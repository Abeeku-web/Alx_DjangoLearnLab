from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet

# Create a router and register the BookViewSet
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    path('books/', BookList.as_view(), name= 'book-list'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'), # Token retrieval endpoint
    path('', include(router.urls)), # This includes all routes registered with the router
]