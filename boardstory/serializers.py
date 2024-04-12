# serializers.py
from rest_framework import serializers
from .models import StoryModel

class StorySerializer(serializers.ModelSerializer):
    class Meta:
        model = StoryModel
        fields = ['id', 'title', 'description','assigned_to','assignee','status','priority','is_visible']  # Include all fields you want to expose in the API
