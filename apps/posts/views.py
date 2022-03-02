from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.views.generic.edit import ModelFormMixin

from .models import Post, Category, Comment
from .forms import CommentForm
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
    context_object_name = 'posts'
    paginate_by = 20
    def get_queryset(self):
        queryset = self.model.objects.filter(archived=False)
        search_query = self.request.GET.get('search', '')
        if search_query:
            queryset = self.model.objects.filter(title__icontains=self.request.GET.get('search', ''),
                                                 archived=False
                                                 ).filter(
                                                    user__username__icontains=self.request.GET.get('search', ''),
                                                    archived=False
                                                )
            return queryset
        category_slug = self.kwargs.get('category_slug')
        if category_slug:
            category = get_object_or_404(Category, slug=category_slug)
            queryset = self.model.objects.filter(
                archived=False,
                category=category)
            return queryset
        return queryset
    def get_context_data(self, *args, **kwargs):
        context = super(AllPostView, self).get_context_data(*args, **kwargs)
        context['search'] = self.request.GET.get('search', '')
        return context



class PostDetailView(LoginRequiredMixin, DetailView):
    template_name = 'post.html'
    model = Post
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super(PostDetailView,self).get_context_data(**kwargs)
        comments = Comment.objects.filter(post=self.get_object())
        context['comments'] = comments
        context['form'] = CommentForm
        return context


class AddCommentView(LoginRequiredMixin, CreateView):

    def post(self, request, pk, *args, **kwargs):
        form = CommentForm(request.POST)
        user = request.user
        post = Post.objects.get(id=pk)
        if form.is_valid():
            Comment.objects.update_or_create(
                user=user,
                post=post,
                comment=request.POST.get('comment')
            )
            return redirect(f'/post/{post.id}/')
        return redirect(f'/post/{post.id}/')


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


class UpdatePost(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'posts/post_edit.html'
    fields = ['category', 'title', 'description', 'archived']
    success_url = reverse_lazy('index')


class AllArchivedPostView(LoginRequiredMixin, ListView, View):
    template_name = 'posts/archived.html'
    model = Post
    form_class = 1
    context_object_name = 'posts'
    paginate_by = 20
    def get_queryset(self):
        queryset = self.model.objects.filter(archived=True, user=self.request.user.id)
        return queryset

class ChangeArchive(LoginRequiredMixin, UpdateView, ModelFormMixin):
    model = Post
    fields = ['archived']


    def get_success_url(self):
        return redirect('archived_post')


