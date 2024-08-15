from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import viewsets

class BaseApiView(viewsets.ViewSet):

    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
