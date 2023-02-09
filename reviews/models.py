from django.db import models
from orders.models import Order
from accounts.models import User
from serviceman.models import Serviceman
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Review(models.Model):
    order = models.OneToOneField(Order, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    serviceman = models.ForeignKey(Serviceman, on_delete=models.SET_NULL, null=True)
    heading = models.CharField(max_length=80,null=True, blank=True)
    review = models.TextField(max_length=1000,null=True, blank=True)
    star = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        self.order.order_number