from django.shortcuts import render, get_object_or_404
from .models import Listings
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import price_choices, state_choices, bed_rooms


def index(request):
    listings = Listings.objects.order_by(
        '-list_date').filter(is_published=True)
    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    page_listings = paginator.get_page(page)
    context = {
        'listings': page_listings
    }

    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    listing = get_object_or_404(Listings, pk=listing_id)
    context = {
        'listing': listing
    }
    return render(request, 'listings/listing.html', context)


def search(request):
    queryset_list = Listings.objects.order_by('-list_date')
    # keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(
                description__icontains=keywords)
# city
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(
                city__iexact=city)
    # state
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_list = queryset_list.filter(
                state__iexact=state)
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(
                bedrooms__lte=bedrooms)
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(
                price__lte=price)

    context = {
        'state_choices': state_choices,
        'bedroom_choices': bed_rooms,
        'price_choices': price_choices,
        'listings': queryset_list,
        'values': request.GET  # for the form to persiste the data
    }
    return render(request, 'listings/search.html', context)
