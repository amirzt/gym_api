from rest_framework.urls import path

from AD import views

urlpatterns = [
    path('admob/', views.get_admob),
    path('custom/', views.get_custom),

]
