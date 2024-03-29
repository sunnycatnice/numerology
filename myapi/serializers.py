from rest_framework import serializers

from myapi.models import Persondata

# Those are classes that are used to create serializers for some models.
# A serializer is a class that converts complex data, such as model instances
# into native Python data types that can then be easily rendered into JSON / other formats.

class peopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persondata
        fields = ('id', 'name', 'surname', 'date')

