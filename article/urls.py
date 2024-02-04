from rest_framework.urls import path

from article import views

urlpatterns = [
    path('list/', views.get_articles),
]