from django.contrib import admin
from django.urls import path, include
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('hire/', hire, name='hire'),
    path('livery/', livery, name='livery'),
    path('shop/', shop, name='shop'),
    path('contact/', contact, name='contact'),





]
