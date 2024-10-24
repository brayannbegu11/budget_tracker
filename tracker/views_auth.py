from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import UserSerializer


    
class RegisterView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]
    print('here is working')
    def post(self, request):
        print('here is working')
        serializer = UserSerializer(data=request.data) #Convert JSON to Python
        print('Is it here')
        if serializer.is_valid():
            user = serializer.save()
            return Response({'user':serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny] #Anyone can access
    
    
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        
        user = User.objects.filter(username=username).first() #Find user
        
        if user is not None and user.check_password(password): #Check the password
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user': {
                    'id': user.id,
                    'username': user.username,
                    'email': user.email,
                }
            })
        return Response({'detail': 'Invalid credentials'}, status = status.HTTP_401_UNAUTHORIZED)