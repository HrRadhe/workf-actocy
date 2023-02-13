from django.shortcuts import render , HttpResponse, redirect
from .models import Review
from orders.models import Order
from django.db.models import Q
from django.contrib import messages
from serviceman.models import Serviceman
from wallet.models import Wallet
from django.core.paginator import Paginator


# Create your views here.
def c_reviews(request):
    reviews = Review.objects.filter(Q(user=request.user) & Q(star__in = [1,2,3,4,5]))

    if reviews.count() > 8:
        nav = True
    else:
        nav = False
    # print(nav)

    paginator = Paginator(reviews,8)
    page_no = request.GET.get('page')
    current_page = paginator.get_page(page_no)
    # print(current_page)

    context= {
        'reviews' : current_page,
        'nav' : nav
    }
    return render(request , 'reviews/c_review.html',context)

def edit_review(request, pk):
    order = Order.objects.get(pk=pk)
    if request.method == 'POST':
        try:
            review = Review.objects.get(order=order)
            w_heading = request.POST.get('heading')
            w_review = request.POST.get('review')
            w_star = request.POST.get('star-value')
            review.heading = w_heading
            review.star = w_star
            review.review = w_review
            review.save()
            messages.success(request , 'Your review is submitted successfully.')
            return redirect('c_reviews')
            # print(review)
        except:
            review = Review.objects.create(user=request.user, serviceman=order.serviceman, order=order)
            w_heading = request.POST.get('heading')
            w_review = request.POST.get('review')
            w_star = request.POST.get('star-value')
            # print(heading, review, star)
            review.heading = w_heading
            review.star = w_star
            review.review = w_review
            review.save()
            messages.success(request , 'Your review is submitted successfully.')

            if int (w_star) >= 3:
                wallet = Wallet.objects.create(user=request.user, serviceman=order.serviceman, order=order, coin = w_star, review=Review.objects.get(order=order))
                # wallet.
                wallet.save()
            return redirect('c_reviews')

    try:
        review = Review.objects.get(order=order)
        star = []
        for i in range(1, review.star+1):
            star.append(i)
        context = {
            'order' : order,
            'review' : review,
            'star' : star
        }
    except:
        context = {'order' : order}
    return render(request, 'reviews/edit_review.html', context)

def c_review_detail(request, pk):
    review = Review.objects.get(pk=pk)
    order = Order.objects.get(order_number=review.order)
    

    context = {
        'order' : order,
        'review' : review,
        # 'nav' : nav
    }
    return render(request , 'reviews/c_reviews_detail.html',context)


def reviews_s(request):
    reviews = Review.objects.filter(Q(serviceman=Serviceman.objects.get(user=request.user)) & Q(star__in = [1,2,3,4,5]))

    if reviews.count() > 8:
        nav = True
    else:
        nav = False
    # print(nav)

    paginator = Paginator(reviews,8)
    page_no = request.GET.get('page')
    current_page = paginator.get_page(page_no)
    # print(current_page)

    context= {
        'reviews' : current_page,
        'nav' : nav
    }
    return render(request , 'reviews/s_reviews.html',context)

def review_detail_s(request, pk):
    review = Review.objects.get(pk=pk)
    order = Order.objects.get(order_number=review.order)
    context = {
        'order' : order,
        'review' : review,
    }
    return render(request , 'reviews/review_detail_s.html',context)

def check(request):
    user = request.user
    if user.role == 1:
        return redirect('reviews_s')
    elif user.role == 2:
        return redirect('c_reviews')