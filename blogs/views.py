from django.shortcuts import render
from django.views import generic
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin

from rules.contrib.views import PermissionRequiredMixin

from .models import BlogPost
from . import blogs_rules
from comments.forms import CommentForm

import datetime


# Create your views here.
class IndexView(generic.ListView):
    model = BlogPost
    context_object_name = 'post_list'
    template_name = 'blogs/index.html'
    paginate_by = 5

    def get_queryset(self):
        return BlogPost.objects.order_by('-pub_date')


class BloggerIndexView(IndexView):
    def get_queryset(self):
        return BlogPost.objects.filter(author__username=self.kwargs['username']).order_by('-pub_date')


class PostDetailView(generic.DetailView):
    model = BlogPost
    template_name = 'blogs/post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['comment_form'] = CommentForm()
        return data


class CreatePostView(PermissionRequiredMixin, generic.edit.CreateView):
    model = BlogPost
    fields = ['title', 'description', 'text', 'pic']
    template_name = 'blogs/new_post.html'
    permission_required = 'blogs.add_post'
    permission_denied_message = 'You need to login to publish your post.'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.pub_date = datetime.datetime.now()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blogs:post', args=(self.object.id,))


class EditPostView(PermissionRequiredMixin, generic.edit.UpdateView):
    model = BlogPost
    fields = ['title', 'description', 'text', 'pic']
    template_name = 'blogs/edit_post.html'
    permission_required = 'blogs.change_post'
    permission_denied_message = 'You have no permissions to edit this post.'

    def get_success_url(self):
        return reverse('blogs:post', args=(self.object.id,))


class DeletePostView(PermissionRequiredMixin, generic.edit.DeleteView):
    model = BlogPost
    template_name = 'blogs/delete_post.html'
    permission_required = 'blogs.delete_post'
    permission_denied_message = 'You have no permissions to delete this post.'
    context_object_name = 'post'

    def get_success_url(self):
        return reverse('blogs:blogger', args=(self.request.user.username,))

