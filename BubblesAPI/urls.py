"""BubblesAPI URL Configuration

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
from  BubblesApp.views import bubbles_data, bubbles_logo, currency_table_logo, header_footer_logo, bubbles_chart

urlpatterns = [
    path('', bubbles_data),
    path('bubbles_logo/<str:img_name>', bubbles_logo),
    path('currency_table_logo/<str:img_name>', currency_table_logo),
    path('header_footer_logo/<str:img_name>', header_footer_logo),
    path('bubbles_chart/<time>/<id>/<file_name>', bubbles_chart),
]
