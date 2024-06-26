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
    try:
        print('Request data:', request.data)  # Log the request data
        print('request.data ', request.data)
        serializer = TaskSerializer(data=request.data)
        print('serializer: ', serializer)
        if serializer.is_valid():
            print('Serializer data:', serializer.validated_data)  # Log the validated serializer data
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print('Serializer errors:', serializer.errors)  # Log the serializer errors
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        print('Error creating task:', e)  # Log any exceptions that occur
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
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
        print('found dog ', dog)
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
def update_task(request, task_id):
    print('Received request to update task with ID:', task_id)
    print('Request data:', request.data)  # Print the request data received

    try:
        task = Task.objects.get(pk=task_id)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = TaskSerializer(task, data=request.data)
    if serializer.is_valid():
        serializer.save()
        print('Task updated successfully:', serializer.data)  # Print the updated task data
        return Response(serializer.data)
    else:
        # Log serializer errors
        print("Serializer Errors:", serializer.errors)
        # You can log the errors to a file or another logging destination as well

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
###################################################################
@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def partial_update_task(request, task_id):
    print('inside partialy_update_task')
    try:
        task = Task.objects.get(pk=task_id)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = TaskSerializer(task, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        # Log serializer errors
        print("Serializer Errors:", serializer.errors)
        # You can log the errors to a file or another logging destination as well

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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