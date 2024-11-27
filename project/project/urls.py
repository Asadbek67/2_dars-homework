"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from .views import (avto_sahifa, admin_haqida, telefonlar, WOMEN_shops, books_shoops, man_shoops,
                    bosh_sahifa1,bosh_sahifa2, bosh_sahifa3, bosh_sahifa4 )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', avto_sahifa),
    path('admin1/', admin_haqida),
    path('tel/', telefonlar),
    path('women/', WOMEN_shops),
    path('books/', books_shoops),
    path('man/', man_shoops),
    path ('bosh1',bosh_sahifa1),
    path('bosh2', bosh_sahifa2),
    path('bosh3', bosh_sahifa3),
    path('bosh4', bosh_sahifa4)

]


