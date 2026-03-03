from .models import Wedding
from rest_framework import serializers

class WeddingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wedding
        fields = '__all__'
