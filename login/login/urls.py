"""login URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import include, path
from social_django.urls import extra
from django.contrib.auth import views as auth_views
from .views import home, complete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name = "accounts/login.html"), name = "login"),
    path('logout/', auth_views.LogoutView.as_view(template_name = "home.html"), name = "logout"),
    path('auth/', include('social_django.urls', namespace = 'social')),
    path('complete/(<str:backend>){0}'.format(extra), complete, name = 'complete'),
    path('', home, name = 'home'),
]
