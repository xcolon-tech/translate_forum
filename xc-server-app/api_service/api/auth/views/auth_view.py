from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework import viewsets
from api_service.serializers import *

class AuthView(ObtainAuthToken, viewsets.ViewSet):
    
    authentication_classes = [TokenAuthentication]

    def get(self, request):
        request.user.auth_token.delete()
        return Response("Success", status=status.HTTP_200_OK)

    def post(self, request, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request':request})
        serializer.is_valid(raise_exception=True)
        user=serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response(token.key)