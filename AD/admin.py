from django.contrib import admin

# Register your models here.
from AD.models import Admob, CustomAd


@admin.register(Admob)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('type', 'code', 'active', 'package_name')
    list_filter = ('package_name',)
    fields = ('type', 'code', 'active', 'package_name')


@admin.register(CustomAd)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'active', 'package_name')
    list_filter = ('package_name',)
    # fields = ('type', 'active', 'package_name', 'content', 'redirect_url')
