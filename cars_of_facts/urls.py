from django.urls import path
from . import views

urlpatterns = [
    path('bmw/', views.bmw_fact),
    path('toyota/', views.toyota_fact),
    path('mercedes/', views.mercedes_fact),
    path('all/', views.all_facts),
]