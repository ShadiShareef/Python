from django.urls import path     
from . import views

urlpatterns = [
    path('', views.root), 
    path('show/new', views.index),
    path('show',views.show)

]