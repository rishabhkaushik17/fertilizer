from os import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_prediction, name='home'),
    path('/answer', views.get_fertilizer_result, name='answer'),
]
