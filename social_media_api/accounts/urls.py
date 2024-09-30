from django.urls import path
from .views import RegisterView, CustomAuthToken, ProfileView, accounts_home, accounts_redirect, FollowUserView, UnfollowUserView, UserListView
from . import views

urlpatterns = [
    path('', accounts_home, name='accounts_home'),  # Handle /api/accounts/ path
    path('', accounts_redirect),  # Redirect /api/accounts/ to /api/accounts/register/
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomAuthToken.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('follow/<int:user_id>/', FollowUserView.as_view(), name='follow_user'),
    path('unfollow/<int:user_id>/', UnfollowUserView.as_view(), name='unfollow_user'),
    path('users/', UserListView.as_view(), name='user_list'),  # List all users
]