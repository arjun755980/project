"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include
from signup import views
# from profile_app import views 
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from rest_framework.routers import DefaultRouter
from signup.api_views import ProfileViewSet


router = DefaultRouter()
router.register(r'profiles',ProfileViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',views.login_view,name='web3'),
    path('edit_profile/<str:user_email>/',views.edit_view,name='profile_edit'),
    path('sign/',views.signup_view,name='web1'),
    path('home/<str:user_email>/',views.home_view,name='home'),
    path('profile/<int:profile_id>/',views.profile_view,name='profile_view'),
    path('welcome/',views.welcome_view,name='welcome'),
    path('profile/<str:email>/', views.profile_details, name='profile_details'),
    path('',views.logout_view,name='web2'),
    path('api/', include(router.urls)),
    path('api-auth/',include('rest_framework.urls')),
    path('admin_login/',views.admin_login, name='web4' ),
    path('dashboard/', views.admin_dashboard, name = 'admin_dashboard'),
    path('profie_creation/',views.create_profie,name = 'web5')
]

if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
