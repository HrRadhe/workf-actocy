from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db.models.fields.related import ForeignKey, OneToOneField

# Create your models here.
class UserManager(BaseUserManager):

    def create_user(self,first_name,last_name,username,email,phone_number,password=None):
        if not email:
            raise ValueError('User must have an email address')

        if not username:
            raise ValueError('User must have an Username')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name = first_name,
            last_name = last_name,
            phone_number = phone_number,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,first_name,last_name,username,email,phone_number,password=None):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
            first_name = first_name,
            last_name = last_name,
            phone_number = phone_number,

        )

        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    SERVICEMAN = 1
    CUSTOMER = 2

    ROLL_CHOICE = (
        (SERVICEMAN,'Serviceman'),
        (CUSTOMER,'Customer'),
    )

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50,unique=True)
    email = models.EmailField(max_length=100,unique=True)
    phone_number = models.CharField(max_length=12 ,unique=True)
    role = models.SmallIntegerField(choices=ROLL_CHOICE,blank=True,null=True)

    #required fields
    date_joined = models.DateField(auto_now_add=True)
    last_login = models.DateField(auto_now_add=True)
    create_date = models.DateField(auto_now_add=True)
    modified_date = models.DateField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)   
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superadmin = models.BooleanField(default=False)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['email','username','first_name','last_name']

    objects = UserManager()

    def __str__(self):
        return self.phone_number

    def has_perm(self,perm,obj=None):
        return self.is_admin

    def has_module_perms(self,app_label):
        return True

    def get_role(self):
        if self.role == 1:
            user_role = 'Serviceman'
        elif self.role == 2:
            user_role = 'Customer'
        return user_role
    
    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

class UserProfile(models.Model):
    # user = OneToOneField(User, on_delete=models.CASCADE, blank = True,null = True)
    user = OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='users/profile_pictures',blank=True,null=True)
    address = models.TextField(max_length=250,blank=True,null=True)
    # address_line_2 = models.TextField(max_length=50,blank=True,null=True)
    state = models.CharField(max_length=15,blank=True,null=True)
    city = models.CharField(max_length=15,blank=True,null=True)
    pin_code = models.CharField(max_length=15,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    
    def __str__(self):
        return self.user.phone_number

