from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from .views import UserViewSet

# from django.urls import path, include

router = routers.DefaultRouter()
router.register('users', UserViewSet,basename = 'userapi')

urlpatterns = [
    path('', include(router.urls))

 ]
