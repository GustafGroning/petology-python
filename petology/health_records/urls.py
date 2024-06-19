from django.urls import path
from . import views

urlpatterns = [
    path('medications/', views.list_medications, name='medication-list'),
    path('medications/create/', views.create_medication, name='medication-create'),
    path('medications/<int:pk>/', views.get_medication, name='medication-detail'),
    path('medications/<int:pk>/update/', views.update_medication, name='medication-update'),
    path('medications/<int:pk>/partial_update/', views.partial_update_medication, name='medication-partial-update'),
    path('medications/<int:pk>/delete/', views.delete_medication, name='medication-delete'),
    path('medications/dog/<int:dog_id>/', views.get_medications_for_dog, name='get_medications_for_dog'),

    path('conditions/', views.list_conditions, name='condition-list'),
    path('conditions/create/', views.create_condition, name='condition-create'),
    path('conditions/<int:pk>/', views.get_condition, name='condition-detail'),
    path('conditions/<int:pk>/update/', views.update_condition, name='condition-update'),
    path('conditions/<int:pk>/partial_update/', views.partial_update_condition, name='condition-partial-update'),
    path('conditions/<int:pk>/delete/', views.delete_condition, name='condition-delete'),
    path('conditions/dog/<int:dog_id>/', views.get_conditions_for_dog, name='get_conditions_for_dog'),

    path('vaccinations/', views.list_vaccinations, name='vaccination-list'),
    path('vaccinations/create/', views.create_vaccination, name='vaccination-create'),
    path('vaccinations/<int:pk>/', views.get_vaccination, name='vaccination-detail'),
    path('vaccinations/<int:pk>/update/', views.update_vaccination, name='vaccination-update'),
    path('vaccinations/<int:pk>/partial_update/', views.partial_update_vaccination, name='vaccination-partial-update'),
    path('vaccinations/<int:pk>/delete/', views.delete_vaccination, name='vaccination-delete'),
    path('vaccinations/dog/<int:dog_id>/', views.get_vaccinations_for_dog, name='get_vaccinations_for_dog'),
]
