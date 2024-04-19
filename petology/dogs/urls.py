from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import register_dog, get_user_dogs, get_dog_by_id, get_all_breeds, update_dog, partial_update_dog, delete_dog

urlpatterns = [
    path('add/', register_dog, name="register_dog"),
    path('all/', get_user_dogs, name='get_user_dogs'),
    path('get/<int:dog_id>/', get_dog_by_id, name='get_dog_by_id'),
    path('update/<int:dog_id>/', update_dog, name='update_dog'),
    path('partial-update/<int:dog_id>/', partial_update_dog, name='partial_update_dog'),
    path('delete/<int:dog_id>/', delete_dog, name='delete_dog'),

    # Breeds
    path('breeds/', get_all_breeds, name='get_all_breeds'),
]
