from django.db.models import Count
from .models import Post
from datetime import datetime, timedelta

def get_popular_post(request):
    posts = Post.objects.filter()
    context = {'popular_posts': posts}
    return context