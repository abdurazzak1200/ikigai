from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', AllPostView.as_view(), name='index'),
    path('<str:category_slug>/', AllPostView.as_view(), name='category_list'),
    path('category-create/', CategoryCreatedView.as_view(), name='category-create'),
    path('post-create/', PostCreatedView.as_view(), name='post-create'),
    path('archived-post', AllArchivedPostView.as_view(), name='archived_post'),
    # path('archive_false/<int:pk>', ChandeArchiveFalse.as_view(), name='archived_false'),
    # path('archive_true/<int:pk>', ChandeArchiveTrue.as_view(), name='archived_true'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='detail_post'),
    path('<int:pk>/add_post/', AddCommentView.as_view(), name='add_comment'),
    path('post-edit/<int:pk>/', views.UpdatePost.as_view(), name='edit-post'),
    path('post/like/<int:post_id>/', like_post, name="like"),

]
