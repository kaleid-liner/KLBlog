from django.urls import path, re_path
from . import views

app_name = 'comments'
urlpatterns = [
    path('post/<int:post_id>/new_comment', views.CommentCreateView.as_view(), name='new_comment'),
]