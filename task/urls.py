from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('register/',views.register, name='register'),

    path('add_task/', views.addTask, name='add_task'),
    path('remove_task/<str:task_id>/', views.removeTask, name="remove_task"),

    path('profile/', views.profile, name='profile'),
]