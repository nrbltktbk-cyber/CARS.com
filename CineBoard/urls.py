from django.urls import path
from .views import *

urlpatterns = [
    path('movie_list/', MovieListView.as_view(), name='movie_list'),
    path('movie/<int:pk>/', MovieDetailView.as_view(), name='movie_detail'),

    path('add/', MovieCreateView.as_view(), name='add_movie'),
    path('edit/<int:pk>/', MovieUpdateView.as_view(), name='edit_movie'),
    path('delete/<int:pk>/', MovieDeleteView.as_view(), name='delete_movie'),

    path('comment/<int:pk>/', AddCommentView.as_view(), name='add_comment'),

    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
]