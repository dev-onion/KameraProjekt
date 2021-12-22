from django.urls import path

from . import views

urlpatterns = [
    path('systemüberwachung/', views.systemueberwachung) #domain.com/systemüberwachung
]
