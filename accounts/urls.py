from django.urls import path
from . import views


urlpatterns = [
    path("", views.accounts_home, name='account_home'),
    path("all_employees/", views.all_employees, name='all_employees'),
    path("all_employees/<int:id>/", views.employees_details, name='employees_details'),
    path("member_list/", views.members, name='member_list'),
    path("<int:id>/", views.member_details, name='member_details'),

    # category
    path("categories/", views.CategoryListView.as_view(), name='category_list'),
    path('new_category/', views.CategoryCreateView.as_view(), name='new_category'),
    path("category/<int:pk>/", views.CategoryDetailView.as_view(), name='category_detail'),
    path("category/<int:pk>/edit", views.CategoryUpdateView.as_view(), name='category_edit'),
    path("category/<int:pk>/delete", views.CategoryDeleteView.as_view(), name='category_delete'),

    # inventory
    path('list_items/', views.list_item, name='list_items'),
    path('cashflow_detail/<str:pk>/', views.cashflow_detail, name="cashflow_detail"),
    path('add_items/', views.add_items, name='add_items'),
    path('update_items/<str:pk>/', views.update_items, name="update_items"),
    path('inflows_items/<str:pk>/', views.inflows_items, name="inflows_items"),
    path('outflows_items/<str:pk>/', views.outflows_items, name="outflows_items"),
    path('list_history/', views.list_history, name='list_history'),

    # cash
    path('cash_items/', views.cash_item, name='cash_items'),
    path('cash_detail/<str:pk>/', views.cash_detail, name="cash_detail"),
    path('issue_cash/<str:pk>/', views.issue_cash, name="issue_cash"),
    path('receive_cash/<str:pk>/', views.receive_cash, name="receive_cash"),
    path('cash_history/', views.cash_history, name='cash_history'),
]