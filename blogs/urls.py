from django.urls import path, include
from . import views

app_name = 'blogs'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('blogger/<username>/', views.BloggerIndexView.as_view(), name='blogger'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post'),
    path('post/new_post/', views.CreatePostView.as_view(), name='new_post'),
    path('post/<int:pk>/delete_post/', views.DeletePostView.as_view(), name='delete_post'),
    path('post/<int:pk>/edit_post/', views.EditPostView.as_view(), name='edit_post'),
]