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

"""
###################################################################
DogHealthIndex requests
###################################################################
"""

"""
Gets only latest row for a specific dog.
"""
# @permission_classes([IsAuthenticated])
def get_latest_row_for_dog(request, dog_id):
    # if request.user.is_authenticated:
    print ('hello this is an end-point!')

"""
get_all_rows_for_dog
"""






"""
###################################################################
HealthIndexQuestion requests
###################################################################
"""

"""
###################################################################
HealthIndexBatch requests
###################################################################
"""