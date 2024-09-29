from django.urls import path
from .views import RegisterView, CustomAuthToken, ProfileView, accounts_home, accounts_redirect

urlpatterns = [
    path('', accounts_home, name='accounts_home'),  # Handle /api/accounts/ path
    path('', accounts_redirect),  # Redirect /api/accounts/ to /api/accounts/register/
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomAuthToken.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
]