from typing import Any
from django.db.models.base import Model as Model
from django.http import Http404
from django.db.models.query import QuerySet
from django.shortcuts import render,redirect
from restaurantapp.models import Restaurant,Table,Menu,Reservation
from restaurantapp.forms import RegistrationForm,LoginForm,TableCreateform,MenuCreateform
from django.views.generic import FormView,TemplateView,ListView,CreateView,DetailView,UpdateView,View
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy,reverse
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404


class signUpView(CreateView):
    template_name="registration.html"
    model=Restaurant
    form_class=RegistrationForm
    success_url=reverse_lazy("signin")
    
# class SignInView(View):
#     template_name = "login.html"

#     def get(self, request, *args, **kwargs):
#         form = LoginForm()
#         return render(request, self.template_name, {"form": form})

#     def post(self, request, *args, **kwargs):
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get("username")
#             password = form.cleaned_data.get("password")
#             try:
#                 restaurant = Restaurant.objects.get(username=username, password=password)
#                 return render(request,"detail.html",{"restaurant":restaurant})
#             except Restaurant.DoesNotExist:
#                 messages.error(request, "Failed to login")
#                 return render(request, self.template_name, {"form": form})

#         return render(request, self.template_name, {"form": form})
    
def SignInView(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            try:
                restaurant = Restaurant.objects.get(username=username)
                if restaurant.password == password:
                    return redirect('detail', pk=restaurant.pk)
                else:
                    messages.error(request, "Failed to login")
            except Restaurant.DoesNotExist:
                messages.error(request, "Failed to login")
        else:
            messages.error(request, "Invalid form submission")

    else:
        form = LoginForm()

    return render(request, 'login.html', {"form": form})
                
    


class RestaurantDetailView(DetailView):
    template_name="detail.html"
    model=Restaurant
    context_object_name="restaurant"


class IndexView(TemplateView):
    template_name="index.html"
    


class TableCreateView(CreateView):
    template_name = "table.html"
    form_class = TableCreateform
    model = Table
    success_url = reverse_lazy("detail")
    
    def form_valid(self, form):         
        id = self.kwargs.get("pk")
        obj = Restaurant.objects.get(id=id)
        form.instance.restaurant = obj
        messages.success(self.request, "Table added successfully")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Table adding failed")
        return super().form_invalid(form)
    
    
    def get_success_url(self):
        id = self.kwargs.get("pk")
        restaurant_object = Restaurant.objects.get(id=id)
        return reverse("detail", kwargs={"pk": restaurant_object.id})
    

class TableListView(ListView):
    model=Table
    template_name="detail.html"
    context_object_name="tables"
    

def TableRemoveView(request, *args, **kwargs):
    id = kwargs.get("pk")
    table_object = Table.objects.get(id=id)
    restaurant_id = table_object.restaurant.id
    table_object.delete()
    return redirect("detail", pk=restaurant_id)



class MenuCreateView(CreateView):
    template_name = "menu.html"
    form_class = MenuCreateform
    model = Menu
    success_url = reverse_lazy("detail")
    
    def form_valid(self, form):         
        id = self.kwargs.get("pk")
        obj = Restaurant.objects.get(id=id)
        form.instance.restaurant = obj
        messages.success(self.request, "Menu added successfully")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Menu adding failed")
        return super().form_invalid(form)
    
    
    def get_success_url(self):
        id = self.kwargs.get("pk")
        restaurant_object = Restaurant.objects.get(id=id)
        return reverse("detail", kwargs={"pk": restaurant_object.id})
    

def MenuRemoveView(request, *args, **kwargs):
    id = kwargs.get("pk")
    menu_object = Menu.objects.get(id=id)
    restaurant_id = menu_object.restaurant.id
    menu_object.delete()
    return redirect("detail", pk=restaurant_id)


class reservationListView(ListView):
    template_name="reservations.html"
    model=Reservation
    context_object_name="reservation"
    
    def get_queryset(self):
        id=self.kwargs.get("pk")
        restaurant_obj =Restaurant.objects.get(id=id)
        qs=Reservation.objects.filter(restaurant=restaurant_obj)
        return qs
    
    

    
    
    