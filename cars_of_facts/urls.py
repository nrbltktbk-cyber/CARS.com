from django.urls import path
from . import views

urlpatterns = [
    path('', views.car_list, name='car_list'),
    path('car/<int:car_id>/', views.car_detail, name='car_detail'),

    path('bmw/', views.bmw_fact, name='bmw'),
    path('toyota/', views.toyota_fact, name='toyota'),
    path('mercedes/', views.mercedes_fact, name='mercedes'),
    path('all/', views.all_facts, name='all_facts'),
]