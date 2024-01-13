from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'dog', 'name', 'location', 'start_time', 'end_time', 'repeat', 'category', 'reminder', 'notes']
