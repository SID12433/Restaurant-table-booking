from django.shortcuts import render,redirect
from restaurantapp.models import User,Restaurant,Menu,Reservation,Table
from userapp.serializer import userRegistration,userLogin,restaurantSerializer,reservationSerializer
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView,CreateAPIView
from rest_framework.viewsets import ViewSet,ModelViewSet
from django.db import transaction
from rest_framework import authentication,permissions
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status
from rest_framework.decorators import action
from django.db.models import Q

# Create your views here.

class signUpView(ListCreateAPIView):
    
    serializer_class=userRegistration
    queryset=User.objects.all()
    
    # def post(self,request,*args,**kwargs):
    #     serializer=userRegistration(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return serializer(data=serializer.data)
    #     else:
    #         return serializer(data=serializer.errors)
    
    
class restaurantView(ViewSet):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    
    def list(self,request,*args,**kwargs):
        qs=Restaurant.objects.all()
        serializer=restaurantSerializer(qs,many=True)
        return Response(data=serializer.data)
    
    def retrieve(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Restaurant.objects.get(id=id)
        serializer=restaurantSerializer(qs)
        return Response(data=serializer.data)
    
    def create(self,request,*args,**kwargs):
        raise serializers.ValidationError("method not allowd")
    def update(self,request,*args,**kwargs):
        raise serializers.ValidationError("method not allowd")
    def destroy(self,request,*args,**kwargs):
        raise serializers.ValidationError("method not allowd")
    
    
    @action(detail=True, methods=['post'])
    def create_reservation(self, request, pk=None):
        id=self.kwargs.get("pk")
        restaurant_obj=Restaurant.objects.get(id=id)
        restaurant = restaurant_obj
        user = request.user
        serializer = reservationSerializer(data=request.data)

        if serializer.is_valid():
            people_count = serializer.validated_data['people_count']
            table = self.get_available_table(restaurant, people_count)

            if table:
                serializer.save(user=user, restaurant=restaurant, table=table)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response({"error": "No available tables for the given people count"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_available_table(self, restaurant, people_count):
        available_table = Table.objects.filter(
            Q(restaurant=restaurant) & (Q(capacity=people_count) | Q(capacity__gt=people_count)) & Q(status="available")
        ).first()
    
        if available_table:
            available_table.status = "booked"
            available_table.save()
    
        return available_table


# from django.views.decorators.csrf import csrf_protect
# class ReservationViewSet(ViewSet):
#     authentication_classes = [authentication.TokenAuthentication]
#     permission_classes = [permissions.IsAuthenticated]
#     @csrf_protect
   

        

