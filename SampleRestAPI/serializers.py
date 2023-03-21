from rest_framework import serializers
from .models import RestAPI

class RestAPISerializer(serializers.ModelSerializer):
    class Meta:
        model = RestAPI
        fields = ['task', 'comleted', 'timestamp', 'updated', 'user']
