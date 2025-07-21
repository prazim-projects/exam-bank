from rest_framework import serializers
from .models import ExamFile


class ExamUploadSerializer(Serializers.ModelSerializer):
    class Meta:
        model = ExamFile
        fields = ['__all__']