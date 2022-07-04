from rest_framework import serializers
from .models import DataPosterTemplate


class DataPosterTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataPosterTemplate
        fields = '__all__'
