from django.urls import path

from . import views

urlpatterns = [
    path('systemüberwachung/', views.systemueberwachung, name='systemüberwachung'),
    path('kamera/', views.kamera, name='kamera')
    ]
