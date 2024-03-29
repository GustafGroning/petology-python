from rest_framework import serializers
from .models import Task
from .models import Dog

class TaskSerializer(serializers.ModelSerializer):
    # Use a PrimaryKeyRelatedField to serialize the dog's primary key
    dog = serializers.PrimaryKeyRelatedField(queryset=Dog.objects.all())

    class Meta:
        model = Task
        fields = ['id', 'dog', 'name', 'location', 'start_time', 'repeat', 'category', 'reminder', 'notes', 'completed']
        read_only_fields = ['dog']
