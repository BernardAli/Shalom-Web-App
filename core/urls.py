from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_page, name='home'),
    path('privacy/', views.privacy, name='privacy'),
    path('career/', views.career, name='career'),
    path('contact/', views.contact, name='contact'),
    path('account/', views.account, name='account'),
    path('account_statement/', views.account_statement, name='account_statement'),
    path('leadership/', views.leadership, name='leadership'),
    path('deacons/', views.deacons_view, name='deacons'),
    path('branches/', views.branches, name='branches'),
    path('working_hours/', views.working_hours, name='working_hours'),
    path('council/', views.council_view, name='council'),
    path('ministries/', views.ministries, name='ministries'),
    path('families/', views.families, name='families'),
    path('members/', views.members, name='members'),
    path('employees/', views.employees, name='employees'),
    path('join/', views.join_view, name='join'),
    path('join_accepted/', views.join_accepted, name='join_accepted'),
    path('service_details/<int:id>/', views.service_details, name='service_details'),
    path('aux_details/<int:id>/', views.aux_details, name='aux_details'),
    path('min_details/<int:id>/', views.min_details, name='min_details'),
    path('family_details/<int:id>/', views.fam_details, name='family_details'),
    path('gallery/', views.gallery, name='gallery'),
    path('books/', views.books, name='books'),
    path('subscribers/', views.subscribers, name='subscribers'),
    path('create_testimony/', views.CreateTestimonyView.as_view(), name='create_testimony'),
    path('history/', views.history, name='history'),
    path('statements/<int:id>/', views.statements, name='statements'),
    path('subscribers_mail/', views.subscribers_mail, name='subscribers_mail'),
]