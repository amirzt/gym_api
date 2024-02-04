from django.contrib import admin

# Register your models here.
from article.models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    list_filter = ('package_name',)
    search_fields = ('title__startswith',)
    fields = ('title', 'time', 'image', 'content', 'package_name')
