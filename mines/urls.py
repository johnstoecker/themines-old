from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('mining', views.mining, name='mining'),
    path('current_mine', views.mining, name='current_mine'),
]
