from django.contrib import admin
from django.urls import path, include
from .views import *


urlpatterns = [
    path('', checkout, name='checkout'),
    path('payment/',payment, name='payment'),
    path('addHorse/<int:pk>', addHorse, name="addHorse"),
    path('success/', success, name='success'),
    path('cancel/', cancel, name='cancel'),





]
