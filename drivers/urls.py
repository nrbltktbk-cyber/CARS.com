from django.urls import path
from . import views

urlpatterns = [
    path('', views.drivers_list, name='drivers_list'),
    path('create/', views.create_driver, name='create_driver'),
    path('update/<int:id>/', views.update_driver, name='update_driver'),
    path('delete/<int:id>/', views.delete_driver, name='delete_driver'),
]