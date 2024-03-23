from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    dog_name = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = ['id', 'dog', 'dog_name', 'name', 'location', 'start_time', 'repeat', 'category', 'reminder', 'notes', 'completed']  # Added 'completed'

    def get_dog_name(self, obj):
        return obj.dog.name
