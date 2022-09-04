from django.urls import path, include
from rest_framework import routers
from .api import (
    UserAPI,
    LoginAPI,
    RegisterAPI,
    GetProfileAPI,
)
from .views import ChangePasswordAPI
from knox import views as knox_views

router = routers.DefaultRouter()
router.register('api/profile', GetProfileAPI, 'profiles')

urlpatterns = [
    path('auth', include('knox.urls')),
    path('auth/register', RegisterAPI.as_view()),
    path('auth/login', LoginAPI.as_view()),
    path('auth/user', UserAPI.as_view()),
    path('auth/logout', knox_views.LogoutView.as_view(), name="knox_logout"),
    path('auth/change-password/', ChangePasswordAPI.as_view(), name='change-password'),
    # path('auth/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
]

urlpatterns += router.urls
