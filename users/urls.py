from django.urls import path, include
from rest_framework import routers
from .api import (
    UserAPI,
    LoginAPI,
    RegisterAPI,
    ProfileViewSet,
)
from knox import views as knox_views

router = routers.DefaultRouter()
router.register('api/profile', ProfileViewSet, 'profiles')

urlpatterns = [
    path('auth', include('knox.urls')),
    path('auth/register', RegisterAPI.as_view()),
    path('auth/login', LoginAPI.as_view()),
    path('auth/user', UserAPI.as_view()),
    path('auth/logout', knox_views.LogoutView.as_view(), name="knox_logout"),
]

urlpatterns += router.urls
