from django.urls import path

from . import views

urlpatterns = [
    path('', views.index), #Home page/
    path('contact', views.contact), #Home page/
]