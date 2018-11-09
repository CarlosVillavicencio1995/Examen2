from django.urls import path
from . import views

urlpatterns = [
    path('', views.Principal, name ='usuarios'),
    path('crear/', views.crear, name ='crear'),
    path('modificar/', views.modificar),
    path('eliminar/', views.eliminar),
]