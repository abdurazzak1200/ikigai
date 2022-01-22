from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from .models import Post

class AllPostView(ListView):
    template_name = 'index.html'
    model = Post
    context_object_name = 'posts'
class PostDetailView(DetailView):
    template_name = 'post.html'
    model = Post
    context_object_name = 'post'


class PostCreatedView(CreateView):
    model = Post
    fields = ['img', 'title', 'description', 'archived']
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PostCreatedView, self).form_valid(form)

