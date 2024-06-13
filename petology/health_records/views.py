from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Medication, Condition, Vaccination
from .serializers import MedicationSerializer, ConditionSerializer, VaccinationSerializer
from django.shortcuts import get_object_or_404

# Medication Views

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_medication(request):
    serializer = MedicationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_medications(request):
    medications = Medication.objects.all()
    serializer = MedicationSerializer(medications, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_medication(request, pk):
    medication = get_object_or_404(Medication, pk=pk)
    serializer = MedicationSerializer(medication)
    return Response(serializer.data)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_medication(request, pk):
    medication = get_object_or_404(Medication, pk=pk)
    serializer = MedicationSerializer(medication, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def partial_update_medication(request, pk):
    medication = get_object_or_404(Medication, pk=pk)
    serializer = MedicationSerializer(medication, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_medication(request, pk):
    medication = get_object_or_404(Medication, pk=pk)
    medication.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

# Condition Views

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_condition(request):
    serializer = ConditionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_conditions(request):
    conditions = Condition.objects.all()
    serializer = ConditionSerializer(conditions, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_condition(request, pk):
    condition = get_object_or_404(Condition, pk=pk)
    serializer = ConditionSerializer(condition)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_conditions_for_dog(request, dog_id):
    conditions = Condition.objects.filter(dog_id=dog_id)
    serializer = ConditionSerializer(conditions, many=True)
    return Response(serializer.data)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_condition(request, pk):
    condition = get_object_or_404(Condition, pk=pk)
    serializer = ConditionSerializer(condition, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def partial_update_condition(request, pk):
    condition = get_object_or_404(Condition, pk=pk)
    serializer = ConditionSerializer(condition, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_condition(request, pk):
    condition = get_object_or_404(Condition, pk=pk)
    condition.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

# Vaccination Views

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_vaccination(request):
    print('reached the back-end')
    serializer = VaccinationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_vaccinations_for_dog(request, dog_id):
    vaccinations = Vaccination.objects.filter(dog_id=dog_id)
    serializer = VaccinationSerializer(vaccinations, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_vaccinations(request):
    vaccinations = Vaccination.objects.all()
    serializer = VaccinationSerializer(vaccinations, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_vaccination(request, pk):
    vaccination = get_object_or_404(Vaccination, pk=pk)
    serializer = VaccinationSerializer(vaccination)
    return Response(serializer.data)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_vaccination(request, pk):
    vaccination = get_object_or_404(Vaccination, pk=pk)
    serializer = VaccinationSerializer(vaccination, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def partial_update_vaccination(request, pk):
    vaccination = get_object_or_404(Vaccination, pk=pk)
    serializer = VaccinationSerializer(vaccination, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_vaccination(request, pk):
    vaccination = get_object_or_404(Vaccination, pk=pk)
    vaccination.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
