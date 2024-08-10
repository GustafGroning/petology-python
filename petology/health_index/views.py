from django.shortcuts import get_object_or_404

from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authtoken.models import Token

from .serializers import DogHealthIndexSerializer, HealthIndexQuestionSerializer, ToothbrushingSerializer
from .models import HealthIndexBatch, DogHealthIndex, HealthIndexQuestion, Dog, Toothbrushing

###################################################################
# DogHealthIndex requests
###################################################################

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_latest_row_for_dog(request, dog_id):
    if request.user.is_authenticated:
        try:
            dog_row = DogHealthIndex.objects.filter(dog=dog_id).latest('date_performed')
            serializer = DogHealthIndexSerializer(dog_row)
            return Response(serializer.data)
        except DogHealthIndex.DoesNotExist:
            return Response(None, status=status.HTTP_200_OK)  # Return null if no row is found

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_all_rows_for_dog(request, dog_id):
    if request.user.is_authenticated:
        dog_rows = DogHealthIndex.objects.filter(dog=dog_id)
        serializer = DogHealthIndexSerializer(dog_rows, many=True)
        return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def save_new_health_index_row(request, dog_id):
    try:
        dog = get_object_or_404(Dog, id=dog_id)
        data = request.data

        # Provide default values if any data is missing
        new_row = DogHealthIndex(
            dog=dog,
            latest_run_batch_id=data.get('latest_run_batch_id', 0),
            date_performed=data.get('date_performed', None),
            general_condition=data.get('general_condition', 1),
            dental_health=data.get('dental_health', 1),
            eyes=data.get('eyes', 1),
            skin_and_coat=data.get('skin_and_coat', 1),
            locomotor_system=data.get('locomotor_system', 1),
            other=data.get('other', 1),
        )

        new_row.save()

        serializer = DogHealthIndexSerializer(new_row)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


###################################################################
# HealthIndexQuestion requests
###################################################################

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_questions_in_batch(request, batch_id):
    batch = get_object_or_404(HealthIndexBatch, id=batch_id)
    question_ids = batch.questions  # Assuming questions is a list of IDs in JSON format
    questions = HealthIndexQuestion.objects.filter(id__in=question_ids)
    serializer = HealthIndexQuestionSerializer(questions, many=True)
    response_data = {
        "batch_id": batch_id,
        "questions": serializer.data
    }
    return Response(response_data, status=status.HTTP_200_OK)


###################################################################
# Toothbrushing requests
###################################################################

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def save_toothbrushing(request, dog_id):
    try:
        dog = get_object_or_404(Dog, id=dog_id)
        data = request.data
        new_toothbrushing = Toothbrushing(
            dog=dog,
            date_performed=data.get('date_performed'),
            streak=data.get('streak', 1)
        )
        new_toothbrushing.save()

        serializer = ToothbrushingSerializer(new_toothbrushing)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_latest_toothbrushing_for_dog(request, dog_id):
    try:
        dog = get_object_or_404(Dog, id=dog_id)
        latest_entry = Toothbrushing.objects.filter(dog=dog).latest('date_performed')
        serializer = ToothbrushingSerializer(latest_entry)
        return Response(serializer.data)
    except Toothbrushing.DoesNotExist:
        return Response({'streak': 0})