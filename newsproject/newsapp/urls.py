from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('category/<str:category_name>/', views.category_news, name='category_news'),
    path('<slug:slug>/', views.news_detail, name='news_detail'),
]