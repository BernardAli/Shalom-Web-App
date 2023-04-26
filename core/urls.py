from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_page, name='home'),
    path('deacons/', views.deacons_view, name='deacons'),
    path('council/', views.council_view, name='council'),
    path('ministries/', views.ministries, name='ministries'),
    path('families/', views.families, name='families'),
    path('members/', views.members, name='members'),
    path('join/', views.join_view, name='join'),
    path('join_accepted/', views.join_accepted, name='join_accepted'),
    path('service_details/<int:id>/', views.service_details, name='service_details'),
    path('aux_details/<int:id>/', views.aux_details, name='aux_details'),
    path('min_details/<int:id>/', views.min_details, name='min_details'),
    path('family_details/<int:id>/', views.fam_details, name='family_details'),
    path('gallery/', views.gallery, name='gallery'),
    path('subscribers/', views.subscribers, name='subscribers'),
    path('create_testimony/', views.CreateTestimonyView.as_view(), name='create_testimony'),
    path('history/', views.history, name='history'),
    path('subscribers_mail/', views.subscribers_mail, name='subscribers_mail'),
]