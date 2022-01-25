from django.db.models import Count
from .models import Category

def get_categoryes(request):
    categoryes = Category.objects.all()
    context = {'categoryes': categoryes}
    return context