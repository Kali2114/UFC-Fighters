from django.core.exceptions import ValidationError
from django.forms import ModelForm, CheckboxSelectMultiple
from .models import Fighter, Comment

class FighterForm(ModelForm):
    class Meta:
        model = Fighter
        fields = '__all__'
        widgets = {
            'fighting_styles': CheckboxSelectMultiple,
        }

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['comment', 'mark']

    def clean_mark(self):
        mark = self.cleaned_data.get('mark')
        if mark is not None and (mark < 1 or mark > 10):
            raise ValidationError("Mark must be between 1 and 10.")
        return mark

    def clean_comment(self):
        comment = self.cleaned_data.get('comment', None)
        if not comment or len(comment) == 0:
            raise ValidationError("Field comment can not be empty.")
        return comment