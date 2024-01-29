from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .forms import FighterForm, CommentForm
from .models import Fighter, Comment

def fighters(request):
    fighters = Fighter.objects.all()
    return render(request, 'base.html', {'fighters': fighters})

@login_required
def add_fighter(request):
    if request.method == 'POST':
        form = FighterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(fighters)
    else:
        form = FighterForm()

    return render(request, 'fighter_form.html', {'form': form, 'new': True})

@login_required
def edit_fighter(request, id):
    fighter = get_object_or_404(Fighter, pk=id)
    if request.method == 'POST':
        form = FighterForm(request.POST, request.FILES, instance=fighter)
        if form.is_valid():
            form.save()
            return redirect(fighters)
    else:
        form = FighterForm(instance=fighter)

    return render(request, 'fighter_form.html', {'form': form, 'new': False})

@login_required
def delete_fighter(request, id):
    fighter = get_object_or_404(Fighter, pk=id)
    if request.method == 'POST':
        fighter.delete()
        return redirect(fighters)

    return render(request, 'delete_fighter.html', {'fighter': fighter})

@login_required()
def fighter_comments(request, fighter_id):
    fighter = get_object_or_404(Fighter, id=fighter_id)
    comments = Comment.objects.filter(fighter=fighter)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.fighter = fighter
            comment.save()
            return redirect('fighter_comments', fighter_id=fighter_id)
        else:
            print("Form is not valid:", form.errors)
    else:
        form = CommentForm()

    return render(request, 'comments.html', {'comments': comments,
                                            'fighter': fighter, 'form': form})

def my_logout(request):
    logout(request)
    return redirect('fighters')

