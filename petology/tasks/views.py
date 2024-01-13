from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Task
from .models import Dog
from .serializers import TaskSerializer

from django.utils.dateparse import parse_datetime
from django.utils import timezone

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

###################################################################
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_task(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
###################################################################
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_tasks(request):
    # Get all dogs that belong to the authenticated user
    user_dogs = Dog.objects.filter(ownerId=request.user)

    # Get all tasks for these dogs
    tasks = Task.objects.filter(dog__in=user_dogs)
    
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

###################################################################
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_tasks_within_timespan(request):
    # Parse timespan from request parameters
    start_time = request.query_params.get('start_time')
    end_time = request.query_params.get('end_time')

    # Convert timespan strings to datetime objects
    if start_time:
        start_time = parse_datetime(start_time)
    if end_time:
        end_time = parse_datetime(end_time)

    # Use current time as default if not provided
    now = timezone.now()
    if not start_time:
        start_time = now
    if not end_time:
        end_time = now

    # Get all dogs that belong to the authenticated user
    user_dogs = Dog.objects.filter(ownerId=request.user)

    # Get all tasks for these dogs within the timespan
    tasks = Task.objects.filter(dog__in=user_dogs, start_time__gte=start_time, end_time__lte=end_time)
    
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

###################################################################
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_tasks_for_dog(request, dog_id):
    # Check if the dog belongs to the authenticated user
    try:
        dog = Dog.objects.get(pk=dog_id, ownerId=request.user)
    except Dog.DoesNotExist:
        return Response({'error': 'Dog not found or not owned by user'}, status=status.HTTP_404_NOT_FOUND)

    # Get all tasks for the specified dog
    tasks = Task.objects.filter(dog=dog)

    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)
###################################################################
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_task(request, task_id):
    try:
        task = Task.objects.get(pk=task_id)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = TaskSerializer(task)
    return Response(serializer.data)
###################################################################
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_task(request, task_id):
    try:
        task = Task.objects.get(pk=task_id)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = TaskSerializer(task, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
###################################################################
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_task(request, task_id):
    try:
        task = Task.objects.get(pk=task_id)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    task.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
###################################################################