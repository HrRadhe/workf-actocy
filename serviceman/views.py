from django.shortcuts import render, redirect ,HttpResponse
from accounts.models import User, UserProfile
from .models import Serviceman
from accounts.forms import userProfileForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from accounts.views import check_role_serviceman
from django.shortcuts import get_object_or_404
from services.models import SubService,MainService
from serviceman.models import Serviceman

from .forms import UserForm

# helper function for get vendor
def get_serviceman(request):
    serviceman = Serviceman.objects.get(user=request.user)
    return serviceman

# Create your views here.
@login_required(login_url='login')
@user_passes_test(check_role_serviceman)
def s_editprofile(request):

    profile = get_object_or_404(UserProfile, user=request.user)
    # print(profile.user)
    serviceman = get_serviceman(request)

    if request.method == 'POST':
        profile_form = UserForm(request.POST, instance=profile.user)
        d_profile_form = userProfileForm(request.POST, request.FILES, instance=profile)

        if profile_form.is_valid() and d_profile_form.is_valid() :
            profile_form.save()
            d_profile_form.save()
            messages.success(request, 'Profile update successfully')
            return redirect('s_editprofie')
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
        'serviceman' : serviceman
    }

    return render(request, 'serviceman/s_editprofile.html', context)


@login_required(login_url='login')
@user_passes_test(check_role_serviceman)
def deleteprofile(request):
    serviceman = get_serviceman(request)
    user= User.objects.get(user=serviceman)
    user.delete()
    messages.success(request, "Your profile has been deleted.")
    return redirect('home')

@login_required(login_url='login')
@user_passes_test(check_role_serviceman)
def my_service(request):
    serviceman = get_serviceman(request)
    print(serviceman.user)
    if request.method == 'POST':
        try:
            get_mainService = request.POST.get("selectedMainService")
            get_subService = request.POST.get("selectedService")

            mainService = MainService.objects.get(user=serviceman)
            mainService.name = get_mainService
            mainService.save()

            subService = SubService.objects.get(serviceman=serviceman)
            subService.name = get_subService
            subService.save()
            messages.success(request, "Your service has been saved.")
            
        except:
            MainService.objects.create(serviceman=serviceman, user= serviceman)
            user = MainService.objects.get(serviceman=serviceman)
            SubService.objects.create(serviceman=serviceman, user=user)
            return redirect('my_service')
        
    return render(request, 'serviceman/my_service.html')
    