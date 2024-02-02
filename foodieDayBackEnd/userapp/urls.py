from django.urls import path
from userapp import views
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register("restaurant",views.restaurantView,basename="restaurant")
# router.register('reservation', views.ReservationViewSet, basename='reservation')


urlpatterns = [
    path("register/",views.signUpView.as_view(),name="register"),
    path("token/",obtain_auth_token),
    
] +router.urls
