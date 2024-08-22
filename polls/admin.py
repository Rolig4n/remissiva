from django.contrib import admin
from django.conf.urls import include
from django.urls import path

# Register your models here.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')),
]