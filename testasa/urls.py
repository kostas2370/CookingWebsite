
from django.contrib import admin
from django.urls import path,include
from users import views as user_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from users.views import UserDetailView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("pro1.urls") ,name="home"),
    path('register/',user_views.register,name="register"),
    path('login/',auth_views.LoginView.as_view(template_name="users/login.html"),name="login"),
    path('logout/',auth_views.LogoutView.as_view(template_name="users/logout.html"),name="logout"),
    path('myprofile/',user_views.profile,name="profile"),
    path('settings/',user_views.settings,name="settings"),
    path('profile/<pk>',UserDetailView.as_view(),name="profile-view") 
    
     ]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)