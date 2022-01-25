from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from .models import Post, Category
from django.shortcuts import get_object_or_404


class AllPostView(LoginRequiredMixin, ListView):
    template_name = 'index.html'
    model = Post
    context_object_name = 'posts'
    def get_queryset(self):
        category_slug = self.kwargs.get('category_slug')
        if category_slug:
            category = get_object_or_404(Category, slug=category_slug)
            queryset = self.model.objects.filter(
                archived=False,
                category=category)
            return queryset
        queryset = self.model.objects.filter(archived=False)
        return queryset



class PostDetailView(LoginRequiredMixin, DetailView):
    template_name = 'post.html'
    model = Post
    context_object_name = 'post'



class PostCreatedView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['category', 'img', 'title', 'description', 'archived']
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PostCreatedView, self).form_valid(form)

#TODO Сделать view редактирования поста

