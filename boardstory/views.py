# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import StoryModel
from .serializers import StorySerializer

class StoryListCreateAPIView(APIView):
    def get(self, request):     
        objects = StoryModel.objects.all()
        serializer = StorySerializer(objects, many=True)
        return Response(serializer.data)
    
    

    def post(self, request):
        serializer = StorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StoryRetrieveUpdateDestroyAPIView(APIView):
    def get_object(self, pk):
        return StoryModel.objects.get(pk=pk)

    def get(self, request, pk):
        obj = self.get_object(pk)
        serializer = StorySerializer(obj)
        return Response(serializer.data)

    def put(self, request, pk):
        obj = self.get_object(pk)
        serializer = StorySerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        obj = self.get_object(pk)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
