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
from .serializers import DogHealthIndexSerializer, HealthIndexQuestionSerializer

# from .models import Dog, Breed
from .models import HealthIndexBatch, DogHealthIndex, HealthIndexQuestion, Dog
# from ..dogs.models import Dog, Breed


###################################################################
# DogHealthIndex requests
###################################################################


"""
Gets only latest row for a specific dog.
"""
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_latest_row_for_dog(request, dog_id):
    if request.user.is_authenticated:
        print('before fetch')
        dog_rows = DogHealthIndex.objects.filter(dog=dog_id).latest('date_performed')
        print('after fetch')
        print('dog_rows ', dog_rows)
        
        serializer = DogHealthIndexSerializer(dog_rows)
        return Response(serializer.data)


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
        # Fetch the dog object
        dog = get_object_or_404(Dog, id=dog_id)

        # Extract data from the request
        data = request.data
        latest_run_batch_id = data.get('latest_run_batch_id')
        batches_in_row = data.get('batches_in_row')
        date_performed = data.get('date_performed')
        general_condition = data.get('general_condition')
        dental_health = data.get('dental_health')
        eyes = data.get('eyes')
        skin_and_coat = data.get('skin_and_coat')
        locomotor_system = data.get('locomotor_system')
        other = data.get('other')

        # Create a new DogHealthIndex row
        new_row = DogHealthIndex.objects.create(
            dog=dog,
            latest_run_batch_id=latest_run_batch_id,
            batches_in_row=batches_in_row,
            date_performed=date_performed,
            general_condition=general_condition,
            dental_health=dental_health,
            eyes=eyes,
            skin_and_coat=skin_and_coat,
            locomotor_system=locomotor_system,
            other=other,
        )

        # Serialize the new row
        serializer = DogHealthIndexSerializer(new_row)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
"""
POST
# New values might be a part of the request?
write_health_index_row(request, dog_id, new_values):
    old_values= get_latest_row_for_dog (so values can be compared)

    dogId = old_values.dog
    new_batch_id -> will either saved this locally or GET does_batch_exist(request, batch_id)
    date_perfomed = Today()
    
    streak = old_values.streak + 1

    for all health_index values:
        general_condition = old_values.general_condition + new_values.general_condition
        probably can't go below 0, right? Check with Ana-Marija
    
    POST/save, whatever django calls it -> (dogId, new_batch_id, date_performed, streak, 
        all_fancy_values)
"""

###################################################################
# HealthIndexQuestion requests
###################################################################
"""
How questions are handled is a bit harder, depends on how we 
decide to handle the front-end.

GET
get_question(request, question_id):
    question = HealthIndexQuestion.question, 
    answers = [each in HealthIndexQuestion.answers]
    return question, answers
"""
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
# HealthIndexBatch requests
###################################################################
"""
GET
This might be the only end-point needed for the model.
We don't care about the batch itself, only the questions in it.    
get_questions_in_batch(request, batch_id):
    return array[question_id1, question_id2, question_id3]

    maybe this could return false if the batch doesn't exist, 
    which means the second end-point doesn't need to exist.
    
GET does_batch_exist(request, batch_id):
    This might be a bad way to handle this, but 
    a call that returns true/false can help determine if
    the batch exists or if current_batch should loop
    around to 1 again.
    return true/false depending on if batch is found.
    might just store the new batch ID locally since I'll have to
    store all the values from questions anyway, but good to have the 
    end-point planned in case it's needed.

"""