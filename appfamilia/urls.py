from re import I
from django.urls import path
from .views import inicio, mi_template

urlpatterns = [
    path('', inicio),
    path('mi-template/', mi_template)
]