from django.urls import path
from . import views

urlpatterns = [
    path('polls/', views.Index, name='polls'),
    path('<int:questions_id>', views.showChoices, name='showchoices'),
    path('<int:questions_id>/result', views.voted, name='voted')
]