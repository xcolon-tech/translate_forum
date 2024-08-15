from rest_framework import serializers
from api_service.models import UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
    
    name = serializers.CharField(required=False)
    mobile = serializers.CharField(required=False)
    email = serializers.CharField(required=False)
    username = serializers.CharField(required=False)
    password = serializers.CharField(required=False)
    bio = serializers.CharField(required=False)
    gender = serializers.CharField(required=False)
    account_status = serializers.PositiveIntegerField(required=False)
    is_active = serializers.PositiveIntegerField(required=False)
    created_at = serializers.DateTimeField(required=False)
    updated_at = serializers.DateTimeField(required=False)
    
    class Meta:
        model = UserProfile
<<<<<<< HEAD
        fields = "__all__"
=======
        fields = "__all__"
        
>>>>>>> 45ebbc3... commit #2 : django server app base > admin rest api impl
