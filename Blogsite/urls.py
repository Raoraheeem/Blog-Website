"""Blogsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from Blogsite import views
from enroll import views as er



urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),
    path('Practice/', views.Practice, name='Practice'),
    path('Education/', views.Education, name='Education'),
    path('Traveling/', views.Traveling, name='Traveling'),
    path('Food/', views.Foods, name='Food'),
    path('History/', views.History, name='History'),
    path('signup/', er.signup, name='signup'),
    path('login/', er.login, name='login'),
    path('profile/',er.profile, name='profile'),
    path('user_logout/',er.user_logout, name='user_logout'),
    path('changepass/',er.changepass, name='changepass'),
    path('userdetail/<int:id>',er.user_detail,name="userdetail")

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
