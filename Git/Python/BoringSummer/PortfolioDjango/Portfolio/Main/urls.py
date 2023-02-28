from django.contrib import admin
from django.urls import path
from Main import views
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static

app_name = 'Main'

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", ),
]
