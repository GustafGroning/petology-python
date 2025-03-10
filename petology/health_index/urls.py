from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from .views import get_all_rows_for_dog, get_latest_row_for_dog, get_questions_in_batch, save_new_health_index_row, save_toothbrushing, get_latest_toothbrushing_for_dog, get_random_question_per_category

urlpatterns = [
   # DogHealthIndex
   path('dog/get/all/<int:dog_id>/', get_all_rows_for_dog, name='get_all_rows_for_dog'),
   path('dog/get/<int:dog_id>/', get_latest_row_for_dog, name="get_latest_row_for_dog"),
   path('batch/get/<int:batch_id>/', get_questions_in_batch, name='get_questions_in_batch'),
   path('dog/<int:dog_id>/add/', save_new_health_index_row, name='save_new_health_index_row'),
   path('questions/get/', get_random_question_per_category, name="get_random_question_per_category"),

   # Toothbrushing
   path('toothbrushing/save/<int:dog_id>/', save_toothbrushing, name='save_toothbrushing'),
   path('toothbrushing/latest/<int:dog_id>/', get_latest_toothbrushing_for_dog, name='get_latest_toothbrushing_for_dog'),

]