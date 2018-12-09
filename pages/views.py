from django.shortcuts import render
from listings.models import Listings
from realtors.models import Realtor
from listings.choices import price_choices, state_choices, bed_rooms
# Create your views here.


def index(request):
    listings = Listings.objects.order_by(
        '-list_date').filter(is_published=True)[:3]
    context = {
        "listings": listings,
        'state_choices': state_choices,
        'bedroom_choices': bed_rooms,
        'price_choices': price_choices
    }
    return render(request, 'pages/index.html', context)


def about(request):
    # get all reators
    realtors = Realtor.objects.order_by('-hire_date')

    # Get MVP
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)
    context = {
        'realtors': realtors,
        'mvp_realtors': mvp_realtors
    }
    return render(request, 'pages/about.html', context)
