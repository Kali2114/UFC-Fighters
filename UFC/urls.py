from django.urls import path
from .views import fighters, add_fighter, edit_fighter, delete_fighter, fighter_comments

urlpatterns = [
    path('fighters/', fighters, name='fighters'),
    path('add_fighter/', add_fighter, name='add_fighter'),
    path('edit_fighter/<int:id>/', edit_fighter, name='edit_fighter'),
    path('delete_fighter/<int:id>/', delete_fighter, name='delete_fighter'),
    path('ufc/fighters/comments/<int:fighter_id>/', fighter_comments, name='fighter_comments'),
]
