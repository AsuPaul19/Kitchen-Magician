from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static
from search import views as search_views
from groups import views as groups_views
from users import views as users_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('search/', search_views.search, name='search'),
    path('groups/', groups_views.groups, name='groups'),
    path('login/', users_views.login, name='login'),
    path('', include('home.urls')),
    path('about/', include('about.urls')),
]

# In DEBUG model, read MEDIA
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)