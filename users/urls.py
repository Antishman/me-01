

from django.urls import path, include
from .views import CustomRegisterView

urlpatterns = [
    path('auth/', include('dj_rest_auth.urls')),  # Login, Logout, Password Reset, etc.
    path('auth/registration/', CustomRegisterView.as_view(), name='custom_register'),  # Custom registration
    path('auth/registration/social/', include('allauth.socialaccount.urls')),  # Social login
]