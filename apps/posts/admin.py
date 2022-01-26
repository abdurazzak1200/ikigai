from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Comment)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("name",)}
    list_display = ("name", "id")

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", 'user', 'category', 'archived')
    list_filter = ('category', 'user')
    search_fields = ['title', 'user__username', 'category__name']
