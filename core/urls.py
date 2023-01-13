from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_page, name='home'),
    path('join/', views.join_view, name='join'),
    path('join_accepted/', views.join_accepted, name='join_accepted'),
]