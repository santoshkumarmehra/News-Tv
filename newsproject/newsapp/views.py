from django.shortcuts import render, get_object_or_404
from .models import NewsItem, Category
from django.utils import timezone

def home(request):
    """View for the homepage."""
    current_date_time = timezone.localtime(timezone.now())
    breaking_news = NewsItem.objects.filter(is_breaking=True).order_by('-pub_date')
    trending_news = NewsItem.objects.filter(is_trending=True).order_by('-pub_date')
    latest_news = NewsItem.objects.exclude(is_breaking=True).exclude(is_trending=True).order_by('-pub_date')
    categories = Category.objects.all()
    context = {
        'current_date_time': current_date_time,
        'breaking_news': breaking_news,
        'trending_news': trending_news,
        'latest_news': latest_news,
        'categories': categories,
    }
    return render(request, 'newsapp/home.html', context)


def category_news(request, category_name):
    """View for displaying news articles within a specific category."""
    current_date_time = timezone.localtime(timezone.now())
    category = get_object_or_404(Category, name=category_name)
    news_items = NewsItem.objects.filter(category=category).order_by('-pub_date')
    categories = Category.objects.all()
    context = {
        'current_date_time': current_date_time,
        'category': category,
        'news_items': news_items,
        'categories': categories,
    }
    return render(request, 'newsapp/category_news.html', context)


def news_detail(request, slug):
    """View for displaying the details of a single news article."""
    current_date_time = timezone.localtime(timezone.now())
    news_item = get_object_or_404(NewsItem, slug=slug)
    categories = Category.objects.all()
    context = {
        'current_date_time': current_date_time,
        'news_item': news_item,
        'categories': categories,
    }
    return render(request, 'newsapp/news_detail.html', context)