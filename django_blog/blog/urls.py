from django.urls import path
from . import views
from .views import CommentCreateView, CommentDeleteView, CommentUpdateView
from django.contrib.auth import views as auth_views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, PostByTagListView

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='comment-create'),
    path('post/<int:post_pk>/comments/<int:pk>/edit/', CommentUpdateView.as_view(), name='comment-update'),
    path('post/<int:post_pk>/comments/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
    path('comment/<int:pk>/update/', views.CommentUpdateView.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment-delete'),
    path('search/', views.search_posts, name='search_posts'),
    path('tags/<slug:tag_slug>/', PostByTagListView.as_view(), name= 'post_by_tag'),
]