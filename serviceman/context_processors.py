from accounts.models import UserProfile
from .models import Serviceman


def get_serviceman(request):
    try:
        serviceman = Serviceman.objects.get(user = request.user)
    except:
        serviceman = None    
    return dict(serviceman=serviceman)