from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from search import views as search_views
from recipe import views as recipe_views
from groups import views as groups_views
from users import views as users_views
from about import views as about_views
from testing import views as testing_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('recipe/', include('recipe.urls')),
    path('team-profile/', about_views.profile, name='profile'), 
    path('groups/', groups_views.groups, name='groups'),
    path('login-signup/', users_views.login_signup, name='login_signup'),
    path('login/', users_views.login, name='login'),
    path('forgot-password/', users_views.forgot_password, name='forgot_password'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('<str:username>/profile/', users_views.user_profile, name='user_profile'), # /account/profile
    path('signup/', users_views.signup, name='signup'),
    path('testing/', testing_views.testing, name='testing'),
    path('', include('home.urls')),
    path('search/', include('search.urls')),
    path('about/', include('about.urls')),
]

# In DEBUG model, read MEDIA
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)