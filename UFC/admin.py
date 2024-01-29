from django.contrib import admin
from .models import Fighter, FighterBelt, Comment, FightingStyle


# admin.site.register(Fighter)

@admin.register(Fighter)
class FighterAdmin(admin.ModelAdmin):
    list_display = ['name', 'country', 'age', 'record']

admin.site.register(FighterBelt)
admin.site.register(Comment)
admin.site.register(FightingStyle)