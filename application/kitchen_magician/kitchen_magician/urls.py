
from django.contrib import admin
from django.urls import path, include

# kitchen_magician project routes default to kitchen app routes
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('kitchen.urls')),
]
