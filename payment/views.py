from contextlib import redirect_stderr
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render,redirect,get_object_or_404
from booking.models import Booking
import os
import stripe
from django.http import JsonResponse
from django.conf import settings
from .forms import MakePaymentForm, OrderForm
# Create your views here.

def success(request):
    booking = request.session['booking_pk']
    bookings = Booking.objects.get(pk=booking) 
    message = "You have booked the arena for:" 
    date = bookings.date.strftime("%m/%d/%Y")
    time=bookings.time.strftime("%H:%M:%S")
    sender = bookings.user_email
    name = bookings.user_name
    subject = "Windward Paddocks Booking"
    send_mail(subject, message + date+time+'  from:'+ name, sender, [sender], fail_silently=False)
    send_mail(subject, message + '  from:'+ name, sender, ['contact@windwardpaddocks.com'], fail_silently=False)
    return render(request,'success.html')

def cancel(request):
    booking = request.session['booking_pk']
    bookings = Booking.objects.get(pk=booking) 
    bookings.delete()

    return render(request,'cancel.html')


def payment(request):
  booking = request.session['booking_pk']
  bookings = Booking.objects.get(pk=booking) 
  print(bookings.user)
  if bookings.total < 24.99:
      price='price_1MLlG3JosIiO9G3w3v1MAXgn'
  else:
      price="price_1MLlHdJosIiO9G3wMMRXsurs"



 
  stripe.api_key = settings.STRIPE_TEST_MODE
  print(settings.STRIPE_TEST_MODE)
  if settings.DEBUG:
            domain = "https://www.windwardpaddocks.com"
  checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price': price,
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=domain + '/payment/success/',
            cancel_url=domain + '/payment/cancel/',
        )
  return redirect(checkout_session.url, code=303)



def checkout(request):
    payment_form = MakePaymentForm()
    order_form = OrderForm()


 
    bookings = request.session['booking_pk']


    bookings = Booking.objects.filter(id=bookings)
   




 
    # if bookings.extra_horse==True:
    #     extraHorse = "Yes"

    return render(request,'checkout.html',{'bookings':bookings,'order_form': order_form, 'payment_form': payment_form,})

def addHorse(request,pk):
    v = request.POST.get('extra')

    Booking.objects.get(id=pk)

  
   
    if v=='on':
       
        b = Booking.objects.get(id=pk)
        b.total = 25  # change field
        b.save() # this will update only

    if v==None:
     
        b = Booking.objects.get(id=pk)
        b.total = 15  # change field
        b.save() # this will update only
     

        
   

    return redirect('checkout')