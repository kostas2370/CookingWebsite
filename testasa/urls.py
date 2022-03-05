
from django.contrib import admin
from django.urls import path,include
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("pro1.urls") ,name="home"),
    path('register/',user_views.register,name="register")
    
]
