"""Portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from argparse import Namespace
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path
from Main import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin_pR2*82/', admin.site.urls),
    path("", views.IndexView.as_view(), name='index'),
    #path('Main/', include("Main.urls", namespace="Main")),
    path("blog/", views.BlogListView.as_view(), name='blog'),
    path("projects/", views.ProjectListView.as_view(), name='project')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
