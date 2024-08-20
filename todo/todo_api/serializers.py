# todo/todo_api/serializers.py
from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ["task", "completed", "timestamp", "updated", "user"]
        extra_kwargs = {
            'user': {'read_only': True},  # Ensure the user field is read-only
        }
