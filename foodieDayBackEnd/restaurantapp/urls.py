from django.urls import path
from restaurantapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path("register/",views.signUpView.as_view(),name="signup"),
    path("index/",views.IndexView.as_view(),name="index"),
    path("restaurant/<int:pk>",views.RestaurantDetailView.as_view(),name="detail"),
    # path("",views.SignInView.as_view(),name="signin"),
    path("",views.SignInView,name="signin"),
    path("restaurant/<int:pk>/menu",views.MenuCreateView.as_view(),name="add_menu"),
    path("restaurant/<int:pk>/menu/remove",views.MenuRemoveView,name="remove_menu"),
    path("restaurant/<int:pk>/table",views.TableCreateView.as_view(),name="add_table"),
    path("restaurant/<int:pk>/table/remove",views.TableRemoveView,name="remove_table"),
    path("restaurant/<int:pk>/reservations",views.reservationListView.as_view(),name="reservation"),
    
    
    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
