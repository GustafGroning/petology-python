from django.urls import path
from .views import register, protected_view, get_username
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', obtain_auth_token, name='api_token_auth'),  # uses DRF's built-in view for token generation on login
    path('getUsername/', get_username, name='getUsername'),

    # Mock view to check if tokens are working or not. Simply returns 200 if a token is accepted.
    path('protected/', protected_view, name='protected_view'),

]