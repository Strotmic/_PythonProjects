from django.urls import path
from . import views
from lijst.views import *

urlpatterns = [
    path('test/', views.lijst2),
    path('platit/', views.it),
    path('personeel/', views.personeel),
    path('refresh/', views.refresh),
  
]