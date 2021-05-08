from rest_framework.serializers import ModelSerializer
from .models import Dog



class DogModelSerializer(ModelSerializer):

    class Meta:
        model=Dog
        fields='__all__'