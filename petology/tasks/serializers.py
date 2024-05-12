from rest_framework import serializers
from .models import Task
from .models import Dog

class TaskSerializer(serializers.ModelSerializer):
    # SerializerMethodField to dynamically add dog_name
    dog_name = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = ['id', 'dog', 'dog_name', 'name', 'location', 'start_time', 'repeat', 'category', 'reminder', 'notes', 'completed']
        # read_only_fields = ['dog']

    def get_dog_name(self, obj):
        return obj.dog.name if obj.dog else None


