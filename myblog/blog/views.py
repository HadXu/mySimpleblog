from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from blog.models import *


# Create your views here.

def home(request):
    post_list = Article.objects.all()
    return render_to_response('index.html', {'post_list': post_list})


def detail(request, id):
    post = Article.objects.get(id=str(id))
    return render_to_response('detail.html', {'post': post})


def get_articles(request, tag_name):
    posts = Article.objects.filter(tag__tag_name=tag_name)
    return render_to_response('index.html', {'post_list': posts})
