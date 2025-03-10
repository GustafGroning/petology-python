from rest_framework import serializers
from .models import DogHealthIndex
from .models import HealthIndexQuestion, Toothbrushing
from articles.serializers import ArticleDetailSerializer
class DogHealthIndexSerializer(serializers.ModelSerializer):
    dog_name = serializers.CharField(source='dog.name')  # Assuming Dog model has a `name` field

    class Meta:
        model = DogHealthIndex
        fields = ['id', 'dog_name', 'latest_run_batch_id', 'batches_in_row', 'date_performed', 'general_condition', 'dental_health', 'eyes', 'skin_and_coat', 'locomotor_system', 'other']



class ResponseSerializer(serializers.Serializer):
    text = serializers.CharField()
    order = serializers.IntegerField()
    value = serializers.CharField()

class HealthIndexQuestionSerializer(serializers.ModelSerializer):
    responses = ResponseSerializer(many=True)
    articles = ArticleDetailSerializer(many=True, read_only=True)
    category = serializers.CharField()

    class Meta:
        model = HealthIndexQuestion
        fields = ['question_title', 'category', 'responses', 'articles']



class ToothbrushingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Toothbrushing
        fields = ['dog', 'date_performed', 'streak']
