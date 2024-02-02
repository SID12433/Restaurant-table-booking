from restaurantapp.models import Restaurant,Table,Menu
from django import forms
from django.contrib.auth.forms import AuthenticationForm



class RegistrationForm(forms.ModelForm):
    class Meta:
        model=Restaurant
        fields="__all__"
        widgets={
            'name': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'description': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'address': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'email': forms.EmailInput(attrs={'class': 'form-control mb-3 mt-3'}),
            'phone': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'username': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control mb-3'}),
        }
        
# class LoginForm(forms.ModelForm):
#     class Meta:
#         model=Restaurant
#         fields=["username","password"]

class LoginForm(forms.Form):
    username=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    password=forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    

class TableCreateform(forms.ModelForm):
    class Meta:
        model=Table
        fields=["table_number","capacity"]

        
class MenuCreateform(forms.ModelForm):
    class Meta:
        model=Menu
        exclude=("restaurant",)
        widgets={
            'name': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'description': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'price': forms.TextInput(attrs={'class': 'form-control mb-3 mt-3'}),
        }