from django.urls import path
from . import views

urlpatterns = [
    # from the index page in listings
    path('', views.index, name='listings'),
    # listings/23(23 is the id)
    path('<int:listing_id>', views.listing, name='listing'),
    path('search', views.search, name='search'),
]
