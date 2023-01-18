from django.db import models
from accounts.models import User, UserProfile

# Create your models here.

class Serviceman(models.Model):
    user = models.OneToOneField(User, related_name="user", on_delete=models.CASCADE)
    user_profile = models.OneToOneField(UserProfile, related_name='userprofile', on_delete=models.CASCADE)
    # serviceman_name= models.CharField(max_length=50)
    serviceman_slug = models.SlugField(max_length=100, unique=True) 
    serviceman_id = models.ImageField(upload_to='vendor/license')
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.serviceman_slug

    class Meta:
        verbose_name_plural = "Servicemen"