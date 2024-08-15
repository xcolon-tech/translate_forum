from rest_framework.response import Response
from rest_framework import status
from api_service.api.auth.views import BaseApiView
from api_service.models import UserProfile
from api_service.api.user_profile.serializers.user_profile_serializers import UserProfileSerializer
from api_service.serializers import *

class UserProfileView(BaseApiView):
    
    def get(self, request, id):
        try:
            model_obj = UserProfile.objects.get(id=id)
        except UserProfile.DoesNotExist:
            return Response(f"User : {id} does not exists", status=status.HTTP_404_NOT_FOUND)
        serializers_obj = UserProfileSerializer(model_obj)
        return Response(serializers_obj.data)
    
    def post(self, request):
        try:
            serializers_obj = UserProfileSerializer(data=request.data)
            if serializers_obj.is_valid():
                serializers_obj.save()
                return Response(serializers_obj.data, status=status.HTTP_201_CREATED)
            
            return Response(serializers_obj.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response("User already exists", status=status.HTTP_404_NOT_FOUND)
        
    def update_name(self, request, id):
        try:
            model_obj = UserProfile.objects.get(id=id)
        except UserProfile.DoesNotExist:
            return Response(f"User :{id} does not exist", status=status.HTTP_404_NOT_FOUND)
        
        serializer_obj = UserProfileSerializer(model_obj, data={'name' : request.data['name']})
        if serializer_obj.is_valid():
            serializer_obj.save()
            return Response(serializer_obj.data)
        
        return Response(serializer_obj.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update_account_status(self, request, id):
        try:
            model_obj = UserProfile.objects.get(id=id)
        except UserProfile.DoesNotExist:
            return Response(f"User :{id} does not exist", status=status.HTTP_404_NOT_FOUND)
        
        serializer_obj = UserProfileSerializer(model_obj, data={'account_status' : request.data['account_status']})
        if serializer_obj.is_valid():
            serializer_obj.save()
            return Response(serializer_obj.data)
        
        return Response(serializer_obj.errors, status=status.HTTP_400_BAD_REQUEST)
    
<<<<<<< HEAD
=======
    def update_mobile_number(self, request, id):
        try:
            model_obj = UserProfile.objects.get(id=id)
        except UserProfile.DoesNotExist:
            return Response(f"User :{id} does not exist", status=status.HTTP_404_NOT_FOUND)
        
        serializer_obj = UserProfileSerializer(model_obj, data={'mobile' : request.data['mobile']})
        if serializer_obj.is_valid():
            serializer_obj.save()
            return Response(serializer_obj.data)
        
        return Response(serializer_obj.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update_email_id(self, request, id):
        try:
            model_obj = UserProfile.objects.get(id=id)
        except UserProfile.DoesNotExist:
            return Response(f"User :{id} does not exist", status=status.HTTP_404_NOT_FOUND)
        
        serializer_obj = UserProfileSerializer(model_obj, data={'email' : request.data['email']})
        if serializer_obj.is_valid():
            serializer_obj.save()
            return Response(serializer_obj.data)
        
        return Response(serializer_obj.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update_username(self, request, id):
        try:
            model_obj = UserProfile.objects.get(id=id)
        except UserProfile.DoesNotExist:
            return Response(f"User :{id} does not exist", status=status.HTTP_404_NOT_FOUND)
        
        serializer_obj = UserProfileSerializer(model_obj, data={'username' : request.data['username']})
        if serializer_obj.is_valid():
            serializer_obj.save()
            return Response(serializer_obj.data)
        
        return Response(serializer_obj.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update_password(self, request, id):
        try:
            model_obj = UserProfile.objects.get(id=id)
        except UserProfile.DoesNotExist:
            return Response(f"User :{id} does not exist", status=status.HTTP_404_NOT_FOUND)
        
        serializer_obj = UserProfileSerializer(model_obj, data={'password' : request.data['password']})
        if serializer_obj.is_valid():
            serializer_obj.save()
            return Response(serializer_obj.data)
        
        return Response(serializer_obj.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update_bio(self, request, id):
        try:
            model_obj = UserProfile.objects.get(id=id)
        except UserProfile.DoesNotExist:
            return Response(f"User :{id} does not exist", status=status.HTTP_404_NOT_FOUND)
        
        serializer_obj = UserProfileSerializer(model_obj, data={'bio' : request.data['bio']})
        if serializer_obj.is_valid():
            serializer_obj.save()
            return Response(serializer_obj.data)
        
        return Response(serializer_obj.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update_user_status(self, request, id):
        try:
            model_obj = UserProfile.objects.get(id=id)
        except UserProfile.DoesNotExist:
            return Response(f"User :{id} does not exist", status=status.HTTP_404_NOT_FOUND)
        
        serializer_obj = UserProfileSerializer(model_obj, data={'is_active' : request.data['is_active']})
        if serializer_obj.is_valid():
            serializer_obj.save()
            return Response(serializer_obj.data)
        
        return Response(serializer_obj.errors, status=status.HTTP_400_BAD_REQUEST)
    
>>>>>>> 45ebbc3... commit #2 : django server app base > admin rest api impl
    def delete_by_id(self, request, id):
        try:
            model_obj = UserProfile.objects.get(id=id)
        except  UserProfile.DoesNotExist:
            return Response(f"User :{id} does not exists", status=status.HTTP_404_NOT_FOUND)
        
        model_obj.delete()        
        return Response("Success", status=status.HTTP_200_OK)
    
    def delete_by_account_status(self, request, account_status):
        models = UserProfile.objects.filter(account_status=account_status)
        models.delete()        
        return Response("Success", status=status.HTTP_200_OK)