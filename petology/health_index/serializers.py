from rest_framework import serializers
from .models import DogHealthIndex

class DogHealthIndexSerializer(serializers.ModelSerializer):
    dog_name = serializers.CharField(source='dog.name')  # Assuming Dog model has a `name` field

    class Meta:
        model = DogHealthIndex
        fields = ['id', 'dog_name', 'latest_run_batch_id', 'batches_in_row', 'date_performed', 'general_condition', 'dental_health', 'eyes', 'skin_and_coat', 'locomotor_system', 'other']
