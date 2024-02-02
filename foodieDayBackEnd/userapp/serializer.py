from rest_framework import serializers
from restaurantapp.models import User,Restaurant,Menu,Table,Reservation

class userRegistration(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    password=serializers.CharField(write_only=True)
    class Meta:
        model=User
        fields=["id","username","email","address","phone","password"]
        
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
        
class userLogin(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["username","password"]
        
class menuSerializer(serializers.ModelSerializer):
    class Meta:
        model=Menu
        fields=["name","description","type","price"]
        
class tableSerializer(serializers.ModelSerializer):
    class Meta:
        model=Table
        fields="__all__"
        
class restaurantSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    menu_items=menuSerializer(many=True,read_only=True)
    table_list=tableSerializer(many=True,read_only=True)
    class Meta:
        model=Restaurant
        fields=["id","name","description","address","email","phone","table_list","menu_items","image"]
        
class reservationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Reservation
        fields=["time","date","people_count"]
