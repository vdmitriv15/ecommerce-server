from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from users.models import User
from products.models import Product
from admins.forms import UserAdminRegistrationForm, UserAdminProfileForm, ProductAddForm


# @user_passes_test(lambda u: u.is_stuff)
def index(request):
    context = {'title': 'GeekShop - Admin'}
    return render(request, 'admins/index.html', context)


# @user_passes_test(lambda u: u.is_stuff)
def admin_users(request):
    context = {
        'title': 'GeekShop - Admin - Users',
        'users': User.objects.all(),
    }
    return render(request, 'admins/admin-users-read.html', context)


# @user_passes_test(lambda u: u.is_stuff)
def admin_users_create(request):
    if request.method == 'POST':
        form = UserAdminRegistrationForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_users'))
    else:
        form = UserAdminRegistrationForm()
    context = {
        'title': 'GeekShop - Admin - User creation form',
        'form': form,
    }
    return render(request, 'admins/admin-users-create.html', context)


# @user_passes_test(lambda u: u.is_stuff)
def admin_users_update(request, pk):
    selected_user = User.objects.get(id=pk)
    if request.method == 'POST':
        form = UserAdminProfileForm(instance=selected_user, files=request.FILES, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_users'))
    else:
        form = UserAdminProfileForm(instance=selected_user)
    context = {
        'title': 'GeekShop - Admin - User update form',
        'form': form,
        'selected_user': selected_user,
    }
    return render(request, 'admins/admin-users-update-delete.html', context)


def admin_users_remove(request, pk):
    selected_user = User.objects.get(id=pk)
    selected_user.is_active = False
    selected_user.save()
    return HttpResponseRedirect(reverse('admins:admin_users'))


class ProductListView(ListView):
    model = Product
    template_name = 'admins/admin-products-read.html'


class ProductCreateView(CreateView):
    model = Product
    template_name = 'admins/admin-products-create.html'
    form_class = ProductAddForm
    success_url = reverse_lazy('admins:admin_products')


class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'admins/admin-products-update-delete.html'
    form_class = ProductAddForm
    success_url = reverse_lazy('admins:admin_products')


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'admins/admin-products-update-delete.html'
    success_url = reverse_lazy('admins:admin_products')
