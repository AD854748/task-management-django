# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CustomUserSerializer
from django.contrib.auth import authenticate

class LoginAPIView(APIView):
    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
       
        try:
            print("serialiser is ",request.data)
            if serializer.is_valid():
                email = serializer.validated_data['email']
                password = serializer.validated_data['password']
                user = authenticate(email=email, password=password)
                print("user is ..",user)
                if user:
                    print("coming here")
                    return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
                else:
                    print("Error : ",serializer.errors)
                    return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print("erroris",e)
           

        
