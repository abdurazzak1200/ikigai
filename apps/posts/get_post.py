from .models import Post

def get_post(request):
    categoryes = Post.objects.all()
    context = {'posts': post}
    return context