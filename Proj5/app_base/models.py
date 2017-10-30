from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfil(models.Model):
    
    user = models.OneToOneField(User)
    
#    additional to user
    
    portfolio_site = models.URLField(blank=True)
    portfolio_pic = models.ImageField(upload_to = 'profile_pic', blank=True)
    
    def __str__(self):
        return self.user.username
        
        
