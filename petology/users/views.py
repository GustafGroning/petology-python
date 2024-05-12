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

###################################################################

@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    if request.method == 'POST':
        email = request.data.get('email')
        password = request.data.get('password')

        if not email or not password:
            return Response({'error': 'Email and password are required'}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(email=email).exists():
            return Response({'error': 'Email already in use'}, status=status.HTTP_400_BAD_REQUEST)

        # Use email as username
        user = User.objects.create_user(username=email, email=email, password=password)
        token, created = Token.objects.get_or_create(user=user)

        return Response({'token': token.key}, status=status.HTTP_201_CREATED)
###################################################################

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def protected_view(request):
    print("Received token:", request.headers.get('Authorization'))
    # Print the request headers
    print("Request headers:", request.headers)
    print("Authorization Header:", request.headers.get('Authorization'))

    # Print the user information if authenticated
    if request.user.is_authenticated:
        print("Authenticated user:", request.user.username)

    # This view requires the user to be authenticated
    return Response({'message': 'You have access to the protected view'}, status=status.HTTP_200_OK)
###################################################################
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_username(request):
    # Check if the user is authenticated
    if request.user.is_authenticated:
        # Return the username of the authenticated user
        return Response({'username': request.user.username}, status=status.HTTP_200_OK)
    else:
        # Return an error response if the user is not authenticated
        return Response({'error': 'User is not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)
###################################################################
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_full_name(request):
    if request.user.is_authenticated:
        full_name = request.user.get_full_name()  # Retrieve full name
        if full_name:
            print('found a full name according to django')
            return Response({'full_name': full_name}, status=status.HTTP_200_OK)
        else:
            # If full_name is not available, return 'N/A'
            print('went into else, will return N/A')
            return Response({'full_name': 'N/A'}, status=status.HTTP_204_NO_CONTENT)
    else:
        # If the user is not authenticated, return an error response
        print('unAuth user')
        return Response({'error': 'User is not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)
###################################################################
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_user_info(request):
    # Check if the request method is PUT
    if request.method == 'PUT':
        # Get the first name and last name from the request data
        first_name = request.data.get('firstName')
        last_name = request.data.get('lastName')

        # Check if both first name and last name are provided
        if not first_name or not last_name:
            return Response({'error': 'First name and last name are required'}, status=status.HTTP_400_BAD_REQUEST)

        # Get the authenticated user
        user = request.user

        # Update the first name and last name of the user
        user.first_name = first_name
        user.last_name = last_name
        user.save()

        return Response({'message': 'User information updated successfully'}, status=status.HTTP_200_OK)
