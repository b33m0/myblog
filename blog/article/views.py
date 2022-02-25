from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ArticleTopic, Article
from .forms import newArticleForm
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.db.models import Q
from comment.models import Comment
from django.contrib.auth.decorators import login_required
import markdown

def a_index(request):
    search = request.GET.get('search')
    order = request.GET.get('order')
    topics = ArticleTopic.objects.all()
    search_t = request.GET.get('search_t')
    a_index = Article.objects.all()


    
    if search:
        print('1')
        if order == 'a_view_count':
            a_index = Article.objects.filter(Q(a_title__icontains=search) | Q(a_content__icontains=search)).order_by('-a_view_count')
        else:
            a_index = Article.objects.filter(Q(a_title__icontains=search) | Q(a_content__icontains=search))
    else:
        print('2')
        if search_t:
            to_search = ArticleTopic.objects.get(t_name = search_t).id
            print(to_search)
            if order == 'a_view_count':
                a_index = a_index.filter(a_topic=to_search).order_by('-a_view_count')
            else:
                a_index = a_index.filter(a_topic=to_search)
            print(a_index)
        else:
            search =''
            if order == 'a_view_count':
                a_index = Article.objects.all().order_by('-a_view_count')
            else:
                a_index = Article.objects.all()

    page = request.GET.get('page')
    paginator = Paginator(a_index, 5) 
    articles = paginator.get_page(page)

    context = { 'articles': articles, 'order': order, 'search': search, 'search_t': search_t, 'topics': topics}
    return render(request, 'article/index.html', context)

def a_detail(request, id):
    article = Article.objects.get(id=id)
    comments = Comment.objects.filter(c_article=id)

    article.a_view_count += 1
    article.save(update_fields=['a_view_count'])
    
    md = markdown.Markdown(
        extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
        ])
    
    article.a_content = md.convert(article.a_content)

    context = { 'article': article, 'toc': md.toc, 'comments':comments}
    return render(request, 'article/detail.html', context)

@login_required(login_url='/userprofile/login/')
def a_create(request):
    if request.method == 'POST':
        new_article_form = newArticleForm(data=request.POST)
        if new_article_form.is_valid():
            new_article = new_article_form.save(commit=False)
            new_article.a_author = User.objects.get(id=request.user.id)
            if request.POST['a_topic'] != None:
                new_article.a_topic = ArticleTopic.objects.get(id=request.POST['a_topic'])
            else:
                return HttpResponse('Please select a topic!')
                
            
            new_article.save()
            return redirect('article:a_index')
        else:
            return HttpResponse('Please input title and content.')
    else:
        new_article_form = newArticleForm()
        topics = ArticleTopic.objects.all()
        context = { 'new_article_form': new_article_form, 'topics': topics}
        return render(request, 'article/post.html', context)

def a_delete(request, id):
    if request.method == 'POST':
        article = Article.objects.get(id=id)
        article.delete()
        return redirect('article:a_index')

def a_modify(request, id):
    m_article = Article.objects.get(id=id)
    if request.method == 'GET':
        a_modify_form = newArticleForm()
        topics = ArticleTopic.objects.all()
        context = { 'article': m_article, 'a_modify_form': a_modify_form, 'topics':topics}
        return render(request, 'article/modify.html', context)
        
    
    elif request.method == 'POST':
        a_modify_form = newArticleForm(data=request.POST)
        if a_modify_form.is_valid():
            m_article.a_title = request.POST['a_title']
            m_article.a_content = request.POST['a_content']

            if request.POST['a_topic']!= 'none':
                m_article.a_topic = ArticleTopic.objects.get(id=request.POST['a_topic'])
            else:
                return HttpResponse('Please select a topic!')

                

            m_article.save()

            return redirect('article:a_detail', id=id)
        else:
            return HttpResponse('Invalid input')
