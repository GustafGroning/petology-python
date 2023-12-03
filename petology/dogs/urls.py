from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import register_dog, get_user_dogs, get_dog_by_id

urlpatterns = [
    path('add/', register_dog, name="register_dog"),
    path('all/', get_user_dogs, name='get_user_dogs'),
    path('get/<int:dog_id>/', get_dog_by_id, name='get_dog_by_id'),


]