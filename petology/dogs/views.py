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
        print('dog sex inside back-end ', request.data.get('sex'))
        name = request.data.get('name')
        breed_name = request.data.get('breed')  # Get breed name from request
        birthday = datetime.strptime(request.data.get('birthday'), '%Y-%m-%d').date()
        sex = request.data.get('sex')  # 1 = male, 2 = female

        # Find the Breed instance
        try:
            breed = Breed.objects.get(name=breed_name)
        except Breed.DoesNotExist:
            return Response({'error': 'Breed not found'}, status=404)

        ownerId = request.user

        # Create the new Dog object
        new_dog = Dog.objects.create(name=name, breed=breed, birthday=birthday, sex=sex, ownerId=ownerId)

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
                'sex': dog.sex,
                'pedigree_name': dog.pedigree_name,                     # New field
                'color': dog.color,                                     # New field
                'insurance_company': dog.insurance_company,             # New field
                'insurance_number': dog.insurance_number,               # New field
                'feed': dog.feed,                                       # New field
                'possible_feed_intolerance': dog.possible_feed_intolerance,  # New field
                'id_number': dog.id_number,
                'registration_number': dog.registration_number,
                'passport_number': dog.passport_number
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
        'sex': dog.sex,
        'pedigree_name': dog.pedigree_name,                     # New field
        'color': dog.color,                                     # New field
        'insurance_company': dog.insurance_company,             # New field
        'insurance_number': dog.insurance_number,               # New field
        'feed': dog.feed,                                       # New field
        'possible_feed_intolerance': dog.possible_feed_intolerance,  # New field
        'id_number': dog.id_number,
        'registration_number': dog.registration_number,
        'passport_number': dog.passport_number
    }
    return Response(dog_data)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_dog(request, dog_id):
    try:
        dog = Dog.objects.get(id=dog_id, ownerId=request.user)
    except Dog.DoesNotExist:
        return Response({'error': 'Dog not found'}, status=status.HTTP_404_NOT_FOUND)

    # Update the fields based on the request data
    dog.name = request.data.get('name', dog.name)

    breed_name = request.data.get('breed')
    if breed_name:
        try:
            print('inside the breed_name thingy')
            breed = Breed.objects.get(name=breed_name)
            dog.breed = breed
        except Breed.DoesNotExist:
            return Response({'error': 'Invalid breed name'}, status=status.HTTP_400_BAD_REQUEST)

    dog.birthday = request.data.get('birthday', dog.birthday)
    dog.sex = request.data.get('sex', dog.sex)
    dog.pedigree_name = request.data.get('pedigree_name', dog.pedigree_name)
    dog.color = request.data.get('color', dog.color)
    dog.insurance_company = request.data.get('insurance_company', dog.insurance_company)
    dog.insurance_number = request.data.get('insurance_number', dog.insurance_number)
    dog.feed = request.data.get('feed', dog.feed)
    dog.possible_feed_intolerance = request.data.get('possible_feed_intolerance', dog.possible_feed_intolerance)
    dog.id_number = request.data.get('id_number', dog.id_number)
    dog.registration_number = request.data.get('registration_number', dog.registration_number)
    dog.passport_number = request.data.get('passport_number', dog.passport_number)

    dog.save()

    return Response({'message': 'Dog updated successfully'}, status=status.HTTP_200_OK)


@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def partial_update_dog(request, dog_id):
    try:
        dog = Dog.objects.get(id=dog_id, ownerId=request.user)
    except Dog.DoesNotExist:
        return Response({'error': 'Dog not found'}, status=404)

    # Update specific fields based on the request data
    if 'name' in request.data:
        dog.name = request.data['name']
    if 'breed' in request.data:
        breed_name = request.data['breed']
        try:
            breed = Breed.objects.get(name=breed_name)
            dog.breed = breed
        except Breed.DoesNotExist:
            return Response({'error': 'Invalid breed name'}, status=status.HTTP_400_BAD_REQUEST)
    if 'birthday' in request.data:
        dog.birthday = request.data['birthday']
    if 'sex' in request.data:
        dog.sex = request.data['sex']
    if 'pedigree_name' in request.data:
        dog.pedigree_name = request.data['pedigree_name']
    if 'color' in request.data:
        dog.color = request.data['color']
    if 'insurance_company' in request.data:
        dog.insurance_company = request.data['insurance_company']
    if 'insurance_number' in request.data:
        dog.insurance_number = request.data['insurance_number']
    if 'feed' in request.data:
        dog.feed = request.data['feed']
    if 'possible_feed_intolerance' in request.data:
        dog.possible_feed_intolerance = request.data['possible_feed_intolerance']
    if 'id_number' in request.data:
        dog.id_number = request.data['id_number']
    if 'registration_number' in request.data:
        dog.registration_number = request.data['registration_number']
    if 'passport_number' in request.data:
        dog.passport_number = request.data['passport_number']

    dog.save()

    return Response({'message': 'Dog updated successfully'}, status=200)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_dog(request, dog_id):
    try:
        # Attempt to retrieve the dog
        dog = Dog.objects.get(id=dog_id, ownerId=request.user)
    except Dog.DoesNotExist:
        # If the dog does not exist, return an error response
        return Response({'error': 'Dog not found'}, status=status.HTTP_404_NOT_FOUND)

    # If the dog exists and belongs to the authenticated user, delete it
    dog.delete()

    # Return a success response
    return Response({'message': 'Dog deleted successfully'}, status=status.HTTP_200_OK)

    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_all_breeds(request):
    breeds = Breed.objects.all()
    breeds_data = [{'id': breed.id, 'name': breed.name} for breed in breeds]
    return Response({'breeds': breeds_data}, status=200)