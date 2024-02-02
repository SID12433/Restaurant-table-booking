from django.contrib import admin
from restaurantapp.models import Restaurant,Table,Menu,Reservation
from django.contrib.auth.models import User



admin.site.register(Restaurant)
admin.site.register(Table)
admin.site.register(Menu)
admin.site.register(User)
admin.site.register(Reservation)
