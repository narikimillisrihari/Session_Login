from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
from app1.serializer import Registerserailizer
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate,login,logout
# Create your views here.

class RegisterUser(APIView):
    permission_classes=[AllowAny]

    def post(self,request):
        serializer=Registerserailizer(data=request.data)

        if serializer.is_valid():
            user=serializer.save()
            return Response({"message":"user registered successfully"},status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors,status=status.HTTP_401_UNAUTHORIZED)

class LoginUser(APIView):
    permission_classes=[AllowAny]

    def post(self,request):
        username=request.data.get("username")
        password=request.data.get("password")
        user=authenticate(username=username,password=password)

        if user:
            login(request, user)  # Create session
            request.session['user_id'] = user.id  # Store user ID in session (optional)
            return Response({"message":"user loging successfully"},status=status.HTTP_200_OK)
        else:
            return Response({"error":"Invalid credentials"},status=status.HTTP_401_UNAUTHORIZED)


class LogoutUser(APIView):
    def post(self,request):
        logout(request)
        return Response({"message":"User logged out successfully"},status=status.HTTP_200_OK)