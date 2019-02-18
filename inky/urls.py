"""inkpressure URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from .views import *
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path(r'base', TemplateView.as_view(template_name='inky/base.html'), name='ink-base'),
    path(r'about', TemplateView.as_view(template_name='inky/about.html'), name='ink-about'),
    path(r'colors', TemplateView.as_view(template_name='inky/colors.html'), name='ink-colors'),
    path(r'css/inkpressure.css', TemplateView.as_view(template_name='inky/inkpressure.css', content_type='text/css'), name='ink-styles'),
    path(r'js/inkpressure.js', TemplateView.as_view(template_name='inky/inkpressure.js', content_type='application/javascript'), name='ink-scripts'),
path(r'', TemplateView.as_view(template_name='inky/home.html'), name='ink-homSe'),
]
