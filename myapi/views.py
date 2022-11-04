from django.http import JsonResponse
from .models import Persondata
from myapi.serializers import peopleSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def person_list(request):
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