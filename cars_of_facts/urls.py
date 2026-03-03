from django.urls import path
from . import views

urlpatterns = [
    path('bmw/', views.bmw_fact),
    path('toyota/', views.toyota_fact),
    path('mercedes/', views.mercedes_fact),
    path('all/', views.all_facts),
    path('', views.car_list_view, name='car_list'),
    path('car/<int:car_id>/', views.car_detail_view, name='car_detail'),
]