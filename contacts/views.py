from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact
from django.contrib.auth.models import User
from django.core.mail import send_mail


def contact(request):
    if request.method == "POST":
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        # check if the user has already make the enquires
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(
                listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(
                    request, 'You have already made an inquriy for this ')
                return redirect('/listings/'+listing_id)

        contact = Contact(listing_id=listing_id, listing=listing, name=name,
                          email=email, phone=phone, message=message, user_id=user_id)
        contact.save()
        send_mail(
            'Property Listing Inquiry',
            'There has been an inquiry for ' + listing +
            ' . Sign into your account for more info',
            'obengstoney@gmail.com',
            [realtor_email, 'bismarkstoney@yahoo.com'],
            fail_silently=False
        )
        messages.success(
            request, 'Your request has been sent a realtor will get to you soon')
        return redirect('/listings/' + listing_id)
