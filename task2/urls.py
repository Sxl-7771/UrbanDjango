# task2/urls.py
from django.urls import path
from .views import ClassBasedView, function_based_view

urlpatterns = [
    path('class/', ClassBasedView.as_view(), name='class_based'),
    path('function/', function_based_view, name='function_based'),
]
