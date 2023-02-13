from django.db import models
from orders.models import Order
from accounts.models import User
from serviceman.models import Serviceman
from reviews.models import Review
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Wallet(models.Model):
    coin = models.SmallIntegerField(validators=[MaxValueValidator(10)])
    order = models.ForeignKey(Order, on_delete=models.SET_NULL ,null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    serviceman = models.ForeignKey(Serviceman, on_delete=models.SET_NULL, null=True)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

