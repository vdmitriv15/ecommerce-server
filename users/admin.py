from django.contrib import admin
from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email')
    fields = (('first_name', 'last_name'), ('username', 'email'), 'image')
    ordering = ('username',)
    search_fields = ('username', 'first_name', 'last_name', 'email')

