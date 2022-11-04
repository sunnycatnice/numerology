from rest_framework import serializers

from myapi.models import Persondata

class peopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persondata
        fields = ('id', 'name', 'description')