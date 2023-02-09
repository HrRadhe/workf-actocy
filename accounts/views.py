from django.shortcuts import render , redirect
from .forms import userForm
from serviceman.forms import ServicemanForm
from .models import User, UserProfile
from django.contrib import messages,auth
from django.template.defaultfilters import slugify
from django.contrib.auth.decorators import login_required, user_passes_test
from .utils import detectuser,send_verification_email
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from orders.models import Order
from django.core.paginator import Paginator
from django.core.exceptions import PermissionDenied
from django.utils.datastructures import MultiValueDictKeyError

def check_role_user(user):
    if user.role == 2:
        return True
    else:
        return PermissionDenied

def check_role_serviceman(user):
    if user.role == 1:
        return True
    else:
        return PermissionDenied


# Create your views here.
def registerUser(request):
    if request.user.is_authenticated:
        messages.warning(request,'You are already logged in.')
        return redirect('myAccount')
    elif request.method == 'POST':
        # print(request.POST)
        form = userForm(request.POST)

        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            password = form.cleaned_data['password']
            user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, phone_number=phone_number, username=username, password=password)
            user.role = User.CUSTOMER
            user.save()

            messages.success(request,"Your registration is complete.")
            return redirect('registerUser')

        else:
            messages.error(request, "Something going  wrong,Please try agings!!")
            print('invalid')
            print(form.errors)
            # return redirect('registerUser')
    else:

        form = userForm()

    context ={
        'form' : form,
    }
    return render(request, 'accounts/user.html' , context)

def registerServiceman(request):
    if request.user.is_authenticated:
        messages.warning(request,'You are already logged in.')
        return redirect('myAccount')
    elif request.method == 'POST':
        print(request.POST)
        form = userForm(request.POST)
        s_form = ServicemanForm(request.POST, request.FILES)

        if form.is_valid() and s_form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            password = form.cleaned_data['password']
            user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, phone_number=phone_number, username=username, password=password)
            user.role = User.SERVICEMAN
            user.save()
            serviceman = s_form.save(commit=False) 
            serviceman.user = user
            serviceman.serviceman_slug = slugify(username)+'-'+str(user.id)
            user_profile = UserProfile.objects.get(user = user)
            serviceman.user_profile = user_profile
            serviceman.save()

            messages.success(request,"Your registration is complete.")
            return redirect('registerServiceman')

        else:
            messages.error(request, "Something going  wrong,Please try agings!!")
            print('invalid')
            print(form.errors)
            # return redirect('registerUser')
    else:

        form = userForm()
        s_form = ServicemanForm()

    context ={
        'form' : form,
        's_form' : s_form,
    }
    return render(request, 'serviceman/serviceman.html', context)

def login(request):
    if request.user.is_authenticated:
        messages.warning(request,'You are already logged in.')
        return redirect('myAccount')
    elif request.method == 'POST': 
        phone_number = request.POST['phone_number']
        password =  request.POST['password']

        user = auth.authenticate(phone_number=phone_number, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Login successful')
            # print(check_role_user(user))
            # print(check_role_serviceman(user))
            return redirect('myAccount')
            
        else:
            messages.error(request, 'invalid login')
            return redirect('login')

    return render(request , 'accounts/login.html')

def logout(request):
    auth.logout(request)
    messages.info(request, 'Logout successful')
    return redirect('login')

@login_required(login_url="login")
def myAccount(request):
    user = request.user
    redirectUrl = detectuser(user)
    return redirect(redirectUrl)

@login_required(login_url='login')
@user_passes_test(check_role_user)  
def customerDashboard(request):
    user = request.user
    orders = Order.objects.filter(user=user, is_ordered=True, status = 'New').order_by('-created_at')
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
    return render(request , 'customers/c_booking.html',context)

@login_required(login_url='login')
@user_passes_test(check_role_serviceman)  
def servicemanDashboard(request):
    return render(request , 'serviceman/s_booking.html')


def forgotpassword(request):
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')

        if User.objects.filter(phone_number=phone_number).exists():
            phone_number = User.objects.get(phone_number=phone_number)
            email = phone_number.email
            user = User.objects.get(email__exact=email)

            # send reset password email
            mail_subject = 'Reset Your Password'
            email_template = 'accounts/emails/reset_password.html'
            send_verification_email(request, user, mail_subject, email_template)

            messages.success(request, 'Password reset link has been sent to your email address.')
            return redirect('login')
        else:
            messages.error(request, 'Account does not exist')
            return redirect('forgot_password')
    return render(request , 'accounts/forgot_password.html')

def reset_password_validate(request, uidb64, token):
    #activate user by setting the is_active status to true
    try:
        # uid = urlsafe_base64_decode(uidb64).decode()
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User._default_manager.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user,token):
        request.session['uid'] = uid
        messages.success(request, 'Reset your password!')
        return redirect('reset_password')
    else:
        messages.error(request, 'Invalid activation link!')
        return redirect('myAccount')
    # return render (request, 'accounts/reset_password_validate.html')
    

def reset_password(request):
    if request.method == 'POST':
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            pk = request.session.get('uid')
            user = User.objects.get(pk=pk)
            user.set_password(password)
            user.save()
            messages.success(request, 'Password reset successfully')
            return redirect('login')
        else:
            messages.error(request, 'Make sure your password and confirm password is same.')
            return redirect('reset_password')
    return render (request, 'accounts/resetPassword.html')
