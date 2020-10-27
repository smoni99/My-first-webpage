from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('Würfel/', views.Würfel),
    path('Hangman_allein/', views.Hangman_allein),
    path('Hangman_für_zwei/', views.Hangman_für_zwei)
]