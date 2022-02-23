from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Post, Category, Comment
from django.shortcuts import get_object_or_404, redirect
from django.shortcuts import get_object_or_404
from django.contrib import admin

def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user.is_authenticated:
        if request.user not in post.likes.all():
            post.likes.add(request.user)
            return redirect("detail_post", post.id)
        else:
            post.likes.remove(request.user)
            return redirect("detail_post", post.id)
    return redirect("login")

class AllPostView(LoginRequiredMixin, ListView, View):
    template_name = 'index.html'
    model = Post
    form_class = 1
    context_object_name = 'posts'
    paginate_by = 20
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
    # def get_context_data(self, **kwargs):
    #     context = super(AllPostView, self).get_context_data(**kwargs)
    #     context = ['search_form'] = self.form_class()



class PostDetailView(LoginRequiredMixin, DetailView):
    template_name = 'post.html'
    model = Post
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super(PostDetailView,self).get_context_data(**kwargs)
        comments = Comment.objects.filter(post=self.get_object())
        context['comments'] = comments
        return context


class PostCreatedView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['category', 'img', 'title', 'description', 'archived']
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PostCreatedView, self).form_valid(form)


class CategoryCreatedView(LoginRequiredMixin, CreateView):
    model = Category
    fields = ['name', 'slug']
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CategoryCreatedView, self).form_valid(form)


class UpdatePost(UpdateView):
    model = Post
    fields = ['category', 'title', 'description', 'archived']
    success_url = reverse_lazy('index')

