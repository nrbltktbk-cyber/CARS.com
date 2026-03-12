from django.urls import path
from . import views

urlpatterns = [
    path('', views.register_candidate, name='register_candidate'),
    path('register/', views.register_candidate, name='register_candidate'),
    path('list/', views.candidate_list, name='candidate_list'),
    
]