from rest_framework import serializers
from myapp.models import Hero

class heroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hero
        fields = ('id', 'name', 'alias')
