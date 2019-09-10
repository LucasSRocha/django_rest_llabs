"""luizalabs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from rest_framework import routers
from .views import UserMagaluAPIView
from .views import WishListAPIView
from .views import ProductAPIView

router = routers.DefaultRouter()

router.register(r'usermagalu', UserMagaluAPIView)
router.register(r'wishlist', WishListAPIView)
router.register(r'product', ProductAPIView)

# <URLPattern '^usermagalu/$' [name='usermagalu-list']>
# api_web_1  |
# api_web_1  | <URLPattern '^usermagalu\.(?P<format>[a-z0-9]+)/?$' [name='usermagalu-list']>
# api_web_1  |
# api_web_1  | <URLPattern '^usermagalu/(?P<pk>[^/.]+)/$' [name='usermagalu-detail']>
# api_web_1  |
# api_web_1  | <URLPattern '^usermagalu/(?P<pk>[^/.]+)\.(?P<format>[a-z0-9]+)/?$' [name='usermagalu-detail']>
# api_web_1  |
# api_web_1  | <URLPattern '^$' [name='api-root']>
# api_web_1  |
# api_web_1  | <URLPattern '^\.(?P<format>[a-z0-9]+)/?$' [name='api-root']>
