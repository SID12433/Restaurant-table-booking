from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator,MaxValueValidator


class User(AbstractUser):
    phone=models.CharField(max_length=100)
    address=models.CharField(max_length=100)

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    opening_time = models.TimeField(default='00:00:01')
    closing_time = models.TimeField(default='23:59:59')
    image = models.ImageField(upload_to="images", null=True)
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    @property
    def menu_items(self):
        qs=self.menuitems.all()
        return qs
    
    @property
    def table_list(self):
        qs=self.tablelist.all()
        return qs
    
class Menu(models.Model):
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=100,null=True)
    options=(
        ("veg","veg"),
        ("nonveg","nonveg")
    )
    type=models.CharField(max_length=100,choices=options,default="veg")
    price=models.PositiveIntegerField()
    restaurant=models.ForeignKey(Restaurant,on_delete=models.CASCADE,related_name="menuitems")
    
    def __str__(self) -> str:
        return self.name
    
    
class Table(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE,related_name="tablelist")
    table_number = models.CharField(max_length=50)
    capacity = models.PositiveIntegerField()
    options = (
        ('available', 'Available'),
        ('booked', 'booked'),
    )
    status = models.CharField(max_length=20, choices=options, default='available')
    
    def __str__(self):
        return self.table_number
    
    
class Reservation(models.Model):
    user=models.CharField(max_length=100)
    restaurant=models.ForeignKey(Restaurant,on_delete=models.CASCADE)
    table=models.ForeignKey(Table,on_delete=models.CASCADE)
    time=models.TimeField()
    date=models.DateField()
    people_count=models.PositiveIntegerField()
    options = (
        ('pending', 'pending'),
        ('reserved', 'reserved'),
    )
    status = models.CharField(max_length=20, choices=options, default='pending')
    
    
