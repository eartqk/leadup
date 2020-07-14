from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name="main"),
    path('policy/', views.policy, name="policy"),
    path('about/', views.about, name="about"),
    path('create_application/', views.createApplication, name='create_application'),
    path('success/', views.success, name="success"),
]
