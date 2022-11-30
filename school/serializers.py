from rest_framework.serializers import ModelSerializer
from .models import Student


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'