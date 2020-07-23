"""dApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.views import View
import polls
from polls.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('signup/', signup, name="signup"),
    path('about/', about, name="about"),
    path(r'shop/<type>', shop, name="shop"),
    path('shopsingle/<id>', shopsingle, name="shopsingle"),
    path('shopsingle/', shopsingle1, name="shopsingle"),
    path('single/', single, name="single"),
    path('blog/', blog, name="blog"),
    path('contact/', contact, name="contact"),
    path('login/', loginx, name="login"),
    path('test/', test, name="test"),
    path('checkout/', checkout, name="checkout"),
    path('product/', product, name="product"),
    path('newlogin/', newLogin.as_view(), name="newLogin"),
    path('polls/', poll.as_view(), name="polls"),
]
