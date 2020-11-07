# kitchen_magician/asgi.py
# Programmer: Jeff C Cheng
# Last Modified: 11/5/2020
# added app urls for kitchen
# added app url for user registration

from django.contrib import admin
from django.urls import path, include

# added to display cover
from django.conf import settings
from django.conf.urls.static import static

# added to display user registration page
from users import views as user_views

# kitchen_magician project routes default to kitchen app routes
urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('', include('kitchen.urls')),
]

# added to display cover
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
