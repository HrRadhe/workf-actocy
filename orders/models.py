from django.db import models
from accounts.models import User
import datetime
from serviceman.models import Serviceman
from django.utils import timezone

# Create your models here.
class Order(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Accepted', 'Accepted'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    serviceman = models.ForeignKey(Serviceman, on_delete=models.CASCADE)
    service = models.CharField(max_length=50)
    order_number = models.CharField(max_length=20)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15, blank=True)
    email = models.EmailField(max_length=50)
    address = models.CharField(max_length=200)
    # country = models.CharField(max_length=15, blank=True)
    state = models.CharField(max_length=15, blank=True)
    city = models.CharField(max_length=50)
    pin_code = models.CharField(max_length=10)
    date = models.DateField(default=datetime.date.today() + datetime.timedelta(days=1))
    status = models.CharField(max_length=15, choices=STATUS, default='New')
    is_ordered = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Concatenate first name and last name
    @property
    def name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.order_number

    def save(self, *args, **kwargs):
        if self.status in ['New', 'Accepted'] and self.date < timezone.now().date():
            self.status = 'Cancelled'
        super().save(*args, **kwargs)