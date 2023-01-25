from django.urls import path
from . import views


urlpatterns = [
    path("", views.accounts_home, name='account_home'),
    path("member_list/", views.members, name='member_list'),
    path("<int:id>/", views.member_details, name='member_details'),
]