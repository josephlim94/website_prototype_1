"""website_prototype_1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import include, path

from django.conf.urls import url
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from quickstart import views as quickstart_views

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', quickstart_views.UserViewSet)
router.register(r'groups', quickstart_views.GroupViewSet)

from organizations.backends import invitation_backend

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
    path('main_app/', include('main_app.urls')),
    path('admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('snippets/', include('snippets.urls')),
    url(r'^accounts/', include('organizations.urls')),
    url(r'^invitations/', include(invitation_backend().get_urls())),
]