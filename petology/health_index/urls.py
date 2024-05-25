from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from .views import get_all_rows_for_dog, get_latest_row_for_dog

urlpatterns = [
   # DogHealthIndex
   path('dog/get/all/<int:dog_id>', get_all_rows_for_dog, name='get_all_rows_for_dog'),
   path('dog/get/<int:dog_id>', get_latest_row_for_dog, name="get_latest_row_for_dog"),
]