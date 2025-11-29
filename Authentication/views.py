from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from.serializers import *
from rest_framework.authtoken.models import Token


class UserView(APIView):

    # CREATE user
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        is_superuser = request.data.get('is_superuser', False)
        if not username or not password:
            return Response({"error": "username and password required"}, status=status.HTTP_400_BAD_REQUEST)
        user = User(username=username, is_superuser=is_superuser)
        user.set_password(password)
        user.save()
        return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)

    # GET user by id
    # def get(self, request, user_id):
    #     try:
    #         user = User.objects.get(id=user_id)
    #         data = {"id": user.id, "username": user.username, "is_superuser": user.is_superuser,"first_name":user.first_name}
    #         return Response(data)
    #     except User.DoesNotExist:
    #         return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

    # GET all users
    def get(self, request):
        users = User.objects.all().values('id', 'username', 'is_superuser', 'first_name')
        return Response(list(users), status=status.HTTP_200_OK)

    # UPDATE user by id
    def put(self, request, user_id):
        try:
            user = User.objects.get(id=user_id)
            user.username = request.data.get('username', user.username)
            if 'password' in request.data:
                user.set_password(request.data['password'])
            user.is_superuser = request.data.get('is_superuser', user.is_superuser)
            user.first_name = request.data.get('first_name', user.first_name)
            user.save()
            return Response({"message": "User updated"})
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

    # DELETE user by id
    def delete(self, request, user_id):
        try:
            user = User.objects.get(id=user_id)
            user.delete()
            return Response({"message": "User deleted"})
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

class UserLoginView(APIView):
    def post(self,request):
    #     user_verification=authenticate(username = request.data.get('username'),password = request.data.get('password'))
    #     if user_verification == None:
    #         return Response("Username OR password is invalid.Try again")
    #     else:
    #         return Response("valid user")

        user_data= CustomToken_Serializer(data=request.data)
        if user_data.is_valid():
            return Response(user_data.validated_data)
        else:
            return Response(user_data.errors)
