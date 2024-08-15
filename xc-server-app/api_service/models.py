from django.db import models

class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    email = models.EmailField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
<<<<<<< HEAD
    bio = models.CharField(max_length=100)
=======
    bio = models.CharField(max_length=250)
>>>>>>> 45ebbc3... commit #2 : django server app base > admin rest api impl
    gender = models.CharField(max_length=20)
    account_status = models.PositiveIntegerField()
    is_active = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
<<<<<<< HEAD
    
=======
    
class AdminProfile(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    email = models.EmailField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    account_status = models.PositiveIntegerField()
    is_active = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
>>>>>>> 45ebbc3... commit #2 : django server app base > admin rest api impl
