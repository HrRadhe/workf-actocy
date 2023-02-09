from accounts.models import User


def get_user(request):
    try:
        user = User.objects.get(phone_number = request.user)
    except:
        user = None    
    return dict(user=user)