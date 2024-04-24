from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    email = models.EmailField(max_length=100, unique = True)
    profile_photo = models.ImageField(upload_to='user/profile_picture', blank = True, null= True)
    bio = models.TextField(max_length=300, blank = True, null = True)



    def __str__(self):
        return self.first_name




class Images(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    image = models.ImageField(upload_to = 'users/posts', blank = True, null = True )
    title = models.CharField(max_length = 50, null=True)
    location = models.CharField(max_length=50, blank = True, null = True)
    description = models.TextField(blank=True, null = True)
    uploaded_at = models.DateTimeField(auto_now_add = True)
    modified_at = models.DateField(auto_now= True)


    def __str__(self):
        return self.title