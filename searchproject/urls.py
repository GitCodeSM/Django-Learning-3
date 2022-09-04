"""searchproject URL Configuration

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
from django.urls import path, include
import searchapp
from searchapp import urls
from searchapp.views import homepage
from searchapp.views import counter
from searchapp.views import register
from searchapp.views import login
from searchapp.views import logout
from searchapp.views import page

urlpatterns = [
    path('', include(searchapp.urls)),
    path('counter/', include(searchapp.urls)),
    path('admin/', admin.site.urls),
    path('register/', include(searchapp.urls)),
    path('login/', include(searchapp.urls)),
    path('logout/', include(searchapp.urls)),
    path('page/<str:pk>', include(searchapp.urls))
    ]
