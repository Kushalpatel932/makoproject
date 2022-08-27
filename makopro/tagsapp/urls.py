from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('base/',views.base_view,name='base'),
    path('',views.index_view,name='index'),
    path('table/',views.user_view,name="table"),
]
