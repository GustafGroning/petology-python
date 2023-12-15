from django.shortcuts import get_object_or_404

from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authtoken.models import Token

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .models import Dog, Breed
from datetime import datetime

###################################################################

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def register_dog(request):
    if request.user.is_authenticated:
        name = request.data.get('name')
        breed_name = request.data.get('breed')  # Get breed name from request
        birthday = datetime.strptime(request.data.get('birthday'), '%Y-%m-%d').date()
        sex = request.data.get('sex')  # 1 = male, 2 = female
        sexAsInt = 1 if sex == 'hane' else 2

        # Find the Breed instance
        try:
            breed = Breed.objects.get(name=breed_name)
        except Breed.DoesNotExist:
            return Response({'error': 'Breed not found'}, status=404)

        ownerId = request.user

        # Create the new Dog object
        new_dog = Dog.objects.create(name=name, breed=breed, birthday=birthday, sex=sexAsInt, ownerId=ownerId)

        # Return the new dog's ID and status_code 200
        return Response({'dog_id': new_dog.id}, status=200)
    else:
        # Handle unauthenticated user
        return Response({'error': 'User not authenticated'}, status=401)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_dogs(request):
    if request.user.is_authenticated:
        user_dogs = Dog.objects.filter(ownerId=request.user)
        dogs_data = []

        for dog in user_dogs:
            dog_data = {
                'id': dog.id,
                'name': dog.name,
                'breed': dog.breed.name,  # Assuming Breed has a 'name' field
                'birthday': dog.birthday,
                'sex': dog.sex
            }
            dogs_data.append(dog_data)

        return Response({'dogs': dogs_data}, status=200)
    else:
        return Response({'error': 'User not authenticated'}, status=401)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_dog_by_id(request, dog_id):
    dog = get_object_or_404(Dog, id=dog_id, ownerId=request.user)
    dog_data = {
        'id': dog.id,
        'name': dog.name,
        'breed': dog.breed.name,  # Accessing the name attribute of the Breed object
        'birthday': dog.birthday,
        'sex': dog.sex
    }
    return Response(dog_data)
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_all_breeds(request):
    breeds = Breed.objects.all()
    breeds_data = [{'id': breed.id, 'name': breed.name} for breed in breeds]
    return Response({'breeds': breeds_data}, status=200)