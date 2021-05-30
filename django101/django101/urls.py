"""django101 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django101.cities.views import index

from django101.cities.views import index, list_phones

urlpatterns = [
    path('admin2/', admin.site.urls),
    path('cities/', include('django101.cities.urls')), # here as a second argument we put the function include with the path to the different urls
    path('', include('django101.people.urls')),

    # path('cities/', index), - tova e prosto primer, no gore e po dobriq nachin, za da ne pishem vseki url rachno
    # path('cities/phones', list_phones) , - tova e prosto primer, no gore e po dobriq nachin, za da ne pishem vseki url rachno
]
