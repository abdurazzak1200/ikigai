from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View

from .models import Profile
from posts.models import Post
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.views.generic.edit import FormView, UpdateView, CreateView



class ProfileLogin(LoginView, View):
    template_name = 'accounts/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_context_data(self, *args, **kwargs):
        context = super(ProfileLogin, self).get_context_data(*args, **kwargs)
        context['users'] = User.objects.all()
        return context

    def get_success_url(self):
      return reverse_lazy('index')

class RegisterPage(FormView):
    template_name = 'accounts/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)

        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('index')
        return super(RegisterPage, self).get(*args, **kwargs)

class UpdateProfileView(UpdateView):
    model = Profile
    fields = ['bg', 'image', 'bio', 'inst']
    success_url = reverse_lazy('index')

class ProfileDetailView(DetailView):
    model = User
    template_name = 'accounts/author.html'
    context_object_name = 'author'
    def get_context_data(self, **kwargs):
        context = super(ProfileDetailView, self).get_context_data()
        profile_posts = Post.objects.filter(archived=False, user=self.object.id)
        context['profile_posts'] = profile_posts
        return context

def update_profile(request, user_id):
    user = User.objects.get(pk=user_id)
    user.save()
