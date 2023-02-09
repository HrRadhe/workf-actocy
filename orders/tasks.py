from celery import task
from .models import Order
import datetime

@task
def cancel_expired_orders():
    orders = Order.objects.filter(is_ordered=True, status__in=['New', 'Accepted'], date__lt=datetime.datetime.today())
    for order in orders:
        order.status = 'Cancelled'
        order.save()
