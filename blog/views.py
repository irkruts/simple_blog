from django.shortcuts import render
from django.views.generic import ListView, DetailView
from . models import Article

class ArticleListView(ListView):
    model = Article
    template_name = 'main_page.html'

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'detail.html'
