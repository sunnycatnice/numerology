from django.http import JsonResponse
from .models import Persondata
from myapi.serializers import peopleSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def person_list(request, format=None):
    #get all the people
    #serialize them
    #return json
    
    if request.method == 'GET':
        people = Persondata.objects.all()
        serializer = peopleSerializer(people, many=True)
        return JsonResponse({"people": serializer.data})
    
    if request.method == 'POST':
        serializer = peopleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def person_detail(request, id, format=None):
    
    try:
        person = Persondata.objects.get(pk=id)
    except person.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = peopleSerializer(person)
        return Response({"person": serializer.data})

    elif request.method == 'PUT':
        serializer = peopleSerializer(person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        person.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    