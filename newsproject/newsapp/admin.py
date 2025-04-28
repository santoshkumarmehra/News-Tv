from django.contrib import admin
from .models import Category, NewsItem

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(NewsItem)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'pub_date', 'is_breaking', 'is_trending', 'author')
    list_filter = ('category', 'is_breaking', 'is_trending', 'pub_date', 'author')
    search_fields = ('title', 'content', 'author')
    prepopulated_fields = {'slug': ('title',)}  # Auto-populate slug field
    date_hierarchy = 'pub_date'  # Add date hierarchy for easier filtering
    ordering = ('-pub_date',)