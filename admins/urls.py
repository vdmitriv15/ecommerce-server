from django.urls import path

from admins.views import admin_users_read, admin_users_create, admin_users_update_delete, index

app_name = 'admins'

urlpatterns = [
    path('', index, name='index'),
    path('users-read/', admin_users_read, name='admin_users_read'),
    path('users-create/', admin_users_create, name='admin_users_create'),
]
