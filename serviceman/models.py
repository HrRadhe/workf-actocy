from django.db import models
from accounts.models import User, UserProfile
from accounts.utils import send_notification


# Create your models here.

class Serviceman(models.Model):
    user = models.OneToOneField(User, related_name="user", on_delete=models.CASCADE)
    user_profile = models.OneToOneField(UserProfile, related_name='userprofile', on_delete=models.CASCADE)
    # serviceman_name= models.CharField(max_length=50)
    serviceman_slug = models.SlugField(max_length=100, unique=True) 
    serviceman_id = models.ImageField(upload_to='serviceman/license')
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user_profile.user.phone_number

    # def save(self,*args,**kwargs):
    #     if self.pk is not None:
    #         #update
    #         orig = Serviceman.objects.get(pk=self.pk)
    #         if orig.is_approved != self.is_approved:
    #             mail_template = 'accounts/emails/admin_approval_email.html'
    #             context = {
    #                     'user' : self.user,
    #                     'is_approved' : self.is_approved,
    #                 }
    #             if self.is_approved == True:
    #                 #send notification
    #                 mail_subject = "Congratulation! Now you can add your work types."
                    
    #                 send_notification(mail_subject, mail_template, context)

    #             else:
    #                 mail_subject = "Sorry ! you a eligible for take any kinds of jobs."
    #                 #send notification is already approved
    #                 send_notification(mail_subject, mail_template, context)

    #     return super(Serviceman, self).save(*args,**kwargs)

    class Meta:
        verbose_name_plural = "Servicemen"