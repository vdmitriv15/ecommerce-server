from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from products.models import Product, ProductCategory
from users.forms import UserRegistrationForm, UserProfileForm
from users.models import User


class UserAdminRegistrationForm(UserRegistrationForm):
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'custom-file-input'}), required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'image', 'first_name', 'last_name', 'password1', 'password2')


class UserAdminProfileForm(UserProfileForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control py-4'}))


class ProductAddForm(ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Enter product name'}))
    description = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Description'}))
    price = forms.DecimalField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Description'}))
    quantity = forms.IntegerField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Description'}))
    image = forms.ImageField(widget=forms.TextInput(attrs={'class': 'custom-file-input'}), required=False)
    category = forms.ChoiceField(widget=forms.Select(attrs={
        'class': 'form-control py-4', 'placeholder': 'Category'}, choices=ProductCategory.objects.all()))

    class Meta:
        model = Product
        fields = ('name', 'description', 'price', 'quantity', 'image', 'category')


