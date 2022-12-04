from django.urls import path
from . import views

urlpatterns = [
    path('', views.ArticleListView.as_view(), name='main_page'),
    path('article/<int:pk>', views.ArticleDetailView.as_view(), name='detail'),
]