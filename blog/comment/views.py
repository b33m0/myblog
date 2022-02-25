from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from article.models import Article
from .forms import CommentForm
from .models import Comment

@login_required(login_url='/userprofile/login/')
def c_create(request, article_id):
    article = get_object_or_404(Article, id=article_id)

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.c_article = article
            new_comment.c_author = request.user
            new_comment.save()
            return redirect(article)
        else:
            return HttpResponse("illegal input")
    else:
        return HttpResponse("illegal request")

def c_delete(request, a_id, c_id):
    article = get_object_or_404(Article, id=a_id)
    if request.method == 'POST':
        comment = Comment.objects.get(id=c_id)
        comment.delete()
        return redirect(article)
    else:
        return HttpResponse("illegal request")

