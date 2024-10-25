from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.Serializer):
    class Meta:
        model = Task
        fields = [
            'title',
            'description',
            'created_at'
        ]
        
    def create(self, validated_data):
        return Task.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance