from django.urls import path
from .views import RegisterView, CustomAuthToken, ProfileView, accounts_home, accounts_redirect
from . import views

urlpatterns = [
    path('', accounts_home, name='accounts_home'),  # Handle /api/accounts/ path
    path('', accounts_redirect),  # Redirect /api/accounts/ to /api/accounts/register/
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomAuthToken.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('follow/<int:user_id>/', views.follow_user, name='follow_user'),
    path('unfollow/<int:user_id>/', views.unfollow_user, name='unfollow_user'),
]