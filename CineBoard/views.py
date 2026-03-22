from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Movie, Comment
from .forms import MovieForm, CommentForm


# список фильмов
class MovieListView(generic.ListView):
    model = Movie
    template_name = 'movie_list.html'
    context_object_name = 'movies'

    def get_queryset(self):
        queryset = Movie.objects.all()

        # 🔍 поиск
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(title__icontains=query)

        # 🎯 фильтр по жанру
        genre = self.request.GET.get('genre')
        if genre:
            queryset = queryset.filter(genre__name=genre)

        # ⭐ сортировка по рейтингу
        return queryset.order_by('-rating')


# детали фильма
class MovieDetailView(generic.DetailView):
    model = Movie
    template_name = 'movie_detail.html'
    context_object_name = 'movie'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context


#  добавить фильм
class MovieCreateView(LoginRequiredMixin, generic.CreateView):
    model = Movie
    form_class = MovieForm
    template_name = 'movie_form.html'
    success_url = reverse_lazy('movie_list')


#  редактировать фильм
class MovieUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Movie
    form_class = MovieForm
    template_name = 'movie_form.html'
    success_url = reverse_lazy('movie_list')


#  удалить фильм
class MovieDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Movie
    template_name = 'movie_confirm_delete.html'
    success_url = reverse_lazy('movie_list')


# добавить комментарий
class AddCommentView(LoginRequiredMixin, generic.CreateView):
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.movie_id = self.kwargs['pk']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('movie_detail', kwargs={'pk': self.kwargs['pk']})


#  регистрация
class RegisterView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')


# логин
class CustomLoginView(LoginView):
    template_name = 'login.html'


# logout
class CustomLogoutView(LogoutView):
    next_page = 'login'