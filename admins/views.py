from django.contrib import messages
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

from users.models import User
from admins.forms import UserAdminRegistrationForm


def index(request):
    context = {'title': 'GeekShop - Admin'}
    return render(request, 'admins/index.html', context)


def admin_users_read(request):
    context = {
        'title': 'GeekShop - Admin - Users',
        'users': User.objects.all(),
    }
    return render(request, 'admins/admin-users-read.html', context)


def admin_users_create(request):
    if request.method == 'POST':
        form = UserAdminRegistrationForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'You registered user')
            return HttpResponseRedirect(reverse('admins:admin_users'))
    else:
        form = UserAdminRegistrationForm()
    context = {
        'title': 'GeekShop - Admin - User creation form',
        'form': form,
    }
    return render(request, 'admins/admin-users-create.html', context)


def admin_users_update_delete(request):

    return render(request, 'admins/admin-users-update-delete.html')
