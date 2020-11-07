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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('search/', search_views.search, name='search'),
    path('recipe/', include('recipe.urls')),
    path('groups/', groups_views.groups, name='groups'),
    path('login-signup/', users_views.login_signup, name='login_signup'),
    # path('login-signup/', auth_views.LoginView.as_view(template_name='login_signup.html'), name='login_signup'),
    path('login/', users_views.login, name='login'),
    # path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('team-profile/', about_views.profile, name='profile'), 
    path('account/profile/', users_views.profile, name='accont_profile'), # /account/profile
    path('signup/', users_views.signup, name='signup'),
    path('', include('home.urls')),
    path('about/', include('about.urls')),
]

# In DEBUG model, read MEDIA
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)