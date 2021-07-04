from rest_framework import serializers
from .models import User
from rest_framework.authtoken.models import Token



class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['Bio', 'Name', 'Email', 'Phone', 'Password']

