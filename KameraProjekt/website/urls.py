from django.urls import path

from . import views

urlpatterns = [
    path('system/', views.system) #domain.com/system
]
