from custom.models import Custom

def get_custom(request):
    custom = Custom.objects.get(id=1)
    context = {'custom': custom}
    return context