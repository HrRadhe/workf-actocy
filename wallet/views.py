from django.shortcuts import render
from .models import Wallet
from django.core.paginator import Paginator
from serviceman.models import Serviceman

# Create your views here.
def wallet(request):
    details = Wallet.objects.filter(serviceman=Serviceman.objects.get(user=request.user))
    total = 0
    for detail in details:
        total = detail.coin + total
    # print(total)

    context = {
        'details' : details,
        'total' : total,
    }
    return render(request, 'wallet/wallet.html',context)