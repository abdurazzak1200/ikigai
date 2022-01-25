from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Profile
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.views.generic.edit import FormView, UpdateView, CreateView


class ProfileLogin(LoginView):
    template_name = 'accounts/login.html'
    fields = '__all__'
    redirect_authenticated_user = True
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

class ProfileCreateView(CreateView):
    model = Profile
    fields = ['user', 'image', 'bio', 'inst']
    template_name = 'accounts/update_profile.html'
    success_url = reverse_lazy('index')

