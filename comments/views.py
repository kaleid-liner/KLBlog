from django.views import generic
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect

from rules.contrib.views import PermissionRequiredMixin

from . import comments_rules
from .models import Comment
from blogs.models import BlogPost
from .forms import CommentForm

import datetime


# Create your views here.
class CommentCreateView(PermissionRequiredMixin, generic.edit.CreateView):
    form_class = CommentForm
    template_name = 'blogs/post_detail.html'
    permission_required = 'comments.add_comment'
    permission_denied_message = 'You need to login to comment.'

    def get(self):
        return HttpResponseRedirect(self.get_success_url())

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.pub_date = datetime.datetime.now()
        post = get_object_or_404(BlogPost, pk=self.kwargs['post_id'])
        form.instance.post = post

        if form.cleaned_data['comment_id']:
            parent_comment = get_object_or_404(Comment, pk=form.cleaned_data['comment_id'])
            form.instance.parent_comment = parent_comment

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blogs:post', args=(self.kwargs['post_id'],)) + '#comments'

