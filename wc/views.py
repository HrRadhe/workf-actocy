from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from serviceman.models import Serviceman
from services.models import MainService,SubService
from accounts.models import User , UserProfile
from django.db.models import Q
from reviews.models import Review

def home(request):
    reviews = Review.objects.all().order_by('-updated_at')[:3]
    context = {
        'reviews' : reviews,
    }
    return render(request, 'home.html',context)

def register(request):
    if request.user.is_authenticated:
        messages.warning(request,'You are already logged in.')
        return redirect('myAccount')
    return render(request, 'select.html')

def search(request):
    
    result = request.GET.get('search')
    # print("search")


    if result == None or result == " ":
        return redirect("home")
    

    else :
        fetch_mainservice = MainService.objects.filter(name__icontains=result).values_list('serviceman' , flat=True)
        fetch_subservice = SubService.objects.filter(name__icontains=result).values_list('serviceman' , flat=True) 
        user_profiles = Serviceman.objects.filter(Q(id__in=fetch_subservice) | Q(id__in=fetch_mainservice)).values_list('user', flat=True)

        fetch_name = User.objects.filter(Q(Q(first_name__icontains=result) | Q(last_name__icontains=result) | Q(id__in=user_profiles)) & Q(Q(role=1)))
        
        # print(user_profiles)

        print(fetch_name)
        # print(fetch_mainservice)
        # print(fetch_subservice)
        # serviceman = fetch_subservice.first()
        # print(serviceman)
        # print(serviceman.user_profile.user.first_name)

        # print(fetch_name.role)
        context = {
            'result': result, 
            'names': fetch_name,
            # 'mainservices': fetch_mainservice,
            # 'subservices': fetch_subservice,
        }
        return render(request, 'search/search.html',context)
        # return render(request, 'search/search.html')
    

def service(request):
    return render(request, 'services.html')

def about_us(request):
    return render(request, 'about-us.html')

def contact_us(request):
    return render(request, 'contact-us.html')