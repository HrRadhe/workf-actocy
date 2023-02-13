from django.shortcuts import render,HttpResponse
from accounts.models import User,UserProfile
from serviceman.models import Serviceman
from services.models import SubService,ServicesImage
from .models import Order
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import orderForm
import datetime
from .utils import generate_oder_number,serviceimg

# Create your views here.
@login_required(login_url='login')
def checkout(request, pk):
    serviceman_url = User.objects.get(pk=pk)
    login_user= User.objects.get(phone_number=request.user)
    serviceman = Serviceman.objects.get(user=serviceman_url)
    user_profile = UserProfile.objects.get(user=login_user)
    services =SubService.objects.get(serviceman=serviceman)

    # print(user_profile.city)
    user_in = {
        'first_name': login_user.first_name,
        'last_name': login_user.last_name,
        'email': login_user.email,
        'phone': login_user.phone_number,
        'address': user_profile.address,
        'state': user_profile.state,
        'city': user_profile.city,
        'pin_code': user_profile.pin_code,
        'date': datetime.date.today() + datetime.timedelta(days=1),
    }

    orderform = orderForm(initial=user_in)
    services_h = []
    for service in services.name.split(', '):
        services_h.append(service)

    context ={
        'user' : login_user,
        'orderform' : orderform,
        'services' : services_h,
        'serviceman' : serviceman,
    }
    return render(request, 'orders/checkout.html',context)

@login_required(login_url='login')
def place_order(request):
    if request.method == 'POST':
        serviceman = Serviceman.objects.get(id=request.POST['serviceman'])
        # print(serviceman)

        form = orderForm(request.POST)
        if form.is_valid():

            order= Order()

            order.date = form.cleaned_data['date']
            order.service = form.cleaned_data['services']
            order.first_name = form.cleaned_data['first_name']
            order.last_name = form.cleaned_data['last_name']
            order.phone = form.cleaned_data['phone']
            order.email = form.cleaned_data['email']
            order.address = form.cleaned_data['address']
            order.state = form.cleaned_data['state']
            order.city = form.cleaned_data['city']
            order.pin_code = form.cleaned_data['pin_code']

            order.serviceman = serviceman
            order.user = request.user
            img = ServicesImage.objects.get(pk=int(serviceimg(order.service)))
            order.img = img

            order.save()
            order.order_number = generate_oder_number(order.id)
            order.is_ordered = True
            order.save()
            

            context ={
                'order' : order,
            }

    return render(request, 'orders/place_order.html', context)