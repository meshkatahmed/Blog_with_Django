from django.db import models
from django.contrib.auth.models import User
from address.models import AddressField
# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='user_profile')
    profile_pic = models.ImageField(upload_to='static/media/images/profilepics')
    address = AddressField(on_delete=models.CASCADE)
