from django.shortcuts import render
from .models import Review
from django.shortcuts import redirect

# Create your views here.
def review_list(request):
    reviews = Review.objects.all()
    context = {
        'reviews' : reviews
    }
    return render(request, 'community/review_list.html', context)

def new_review(request):
    return render(request, 'community/new_review.html')

def create_review(request):
    review = Review()
    review.title = request.GET.get('title')
    review.content = request.GET.get('content')
    review.rank = request.GET.get('rank')
    review.save()
    return redirect(f'/community/review_detail/{review.pk}/')

def review_detail(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    context = {
        'review' : review
    }
    return render(request, 'community/review_detail.html', context)