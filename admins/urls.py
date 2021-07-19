from django.urls import path

from admins.views import admin_users, admin_users_create, admin_users_update, index, admin_users_remove,\
    ProductListView, ProductCreateView, ProductUpdateView, ProductDeleteView

app_name = 'admins'

urlpatterns = [
    path('', index, name='index'),
    path('users/', admin_users, name='admin_users'),
    path('users/create/', admin_users_create, name='admin_users_create'),
    path('users/update/<int:pk>/', admin_users_update, name='admin_users_update'),
    path('users/remove/<int:pk>/', admin_users_remove, name='admin_users_remove'),
    path('products/', ProductListView.as_view(), name='admin_products'),
    path('products/create/', ProductCreateView.as_view(), name='admin_products_create'),
    path('products/update/<int:pk>/', ProductUpdateView.as_view(), name='admin_products_update'),
    path('products/remove/<int:pk>/', ProductDeleteView.as_view(), name='admin_products_remove'),
]
