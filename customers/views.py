from django.shortcuts import render, redirect, get_object_or_404,HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from accounts.models import UserProfile, User
from accounts.forms import userProfileForm
from serviceman.forms import UserForm
from orders.models import Order
from serviceman.models import Serviceman
from django.core.paginator import Paginator
from django.http import JsonResponse


# Create your views here.
@login_required(login_url="login")
def c_editprofile(request):
    profile = get_object_or_404(UserProfile, user=request.user)


    if request.method == 'POST':
        profile_form = UserForm(request.POST, instance=profile.user)
        d_profile_form = userProfileForm(request.POST, request.FILES, instance=profile)
        if profile_form.is_valid() and d_profile_form.is_valid() :
            profile_form.save()
            d_profile_form.save()
            messages.success(request, 'Profile update successfully')
            return redirect('c_editprofile')
        else:
            print(profile_form.errors)
            print(d_profile_form.errors)
    else:
        profile_form = UserForm(instance=profile.user)
        # print(profile_form)
        d_profile_form = userProfileForm(instance=profile)
    context = {
        'd_profile_form' : d_profile_form,
        'profile_form' : profile_form,
        'profile' : profile,
        # 'serviceman' : serviceman
    }
    return render(request , 'customers/c_editprofile.html', context)

@login_required(login_url="login")
def pending_order(request, pk):
    order = Order.objects.get(pk=pk)
    context = {
        'order' : order,
    }
    return render(request, 'orders/order_detail.html', context) 

@login_required(login_url='login')
def all_booking(request):
    user = request.user
    orders = Order.objects.filter(user=user, is_ordered=True).exclude(status = 'New').order_by('-updated_at')
    # print(orders)
    if orders.count() > 10:
        nav = True
    else:
        nav = False
    # print(nav)

    paginator = Paginator(orders,10)
    page_no = request.GET.get('page')
    current_page = paginator.get_page(page_no)

    context = {
        'orders' : current_page,
        'nav' : nav,
    }
    return render(request, 'customers/all_booking.html',context)

def cancel_order(request, pk):
    order = Order.objects.get(pk=pk)
    order.status = 'Cancelled'
    order.save()
    return JsonResponse({'success': True})

def c_delete_profile(request):
    user = request.user
    duser = User.objects.get(phone_number=user)
    print(duser)
    duser.delete()
    messages.success(request, "Account Deleted.")
    return redirect('home')
    

def order_detail(request, pk):
    order = Order.objects.get(pk=pk)
    context ={
        'order': order,
    }
    return render(request, 'orders/a_order_detail.html', context)