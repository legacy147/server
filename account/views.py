
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, GenericAPIView
from rest_framework import serializers
from .models import User 
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.response import Response


# Create your views here.

class userserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
    
    def create(self,data):  
        newuser = User.objects.create_user(
            first_name = data['first_name'],
            last_name = data['last_name'],
            email = data['email'],
            password = data['password'],
            image = data['image']
    
        ) 
        
        return newuser
        
    # def validate(self, data):
    #     first_name = data['first_name']
        
    #     if first_name != 'david':
    #         raise serializers.ValidationError("first_name must be david")  

class Signup(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = userserializer   

class UserView(RetrieveUpdateDestroyAPIView):     
    queryset = User.objects.all()
    serializer_class = userserializer  
    permission_class = [IsAuthenticated]   
    
    
class fetchuser(GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = userserializer
    
    def get(self, request):
        print(request.user.id)
        
        user = User.objects.get(id = request.user.id)
        serializer = self.serializer_class(user)
        
        return Response(data = serializer.data, status=200)