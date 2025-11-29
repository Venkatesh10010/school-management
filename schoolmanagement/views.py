from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView


class LoginView(APIView):
    permission_classes = []  # Public access for login

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        userobj = authenticate(username=username, password=password)

        if userobj:
            token, created = Token.objects.get_or_create(user=userobj)
            return Response({"token": token.key}, status=status.HTTP_200_OK)

        return Response({"error": "Invalid Credentials"}, status=status.HTTP_400_BAD_REQUEST)
