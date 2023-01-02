from django.shortcuts import render
import json
import requests
from django.core.mail import send_mail

from django.conf import settings
# Create your views here.
def home(request):
    # fb_access = settings.FB_ACCESS
    if request.method == 'POST':
    
     message = request.POST.get('message')
     sender = request.POST.get('email')
     name = request.POST.get('name')
     subject = request.POST.get('subject')
     send_mail(subject, message + '  from:'+ name, sender, ['contact@windwardpaddocks.com'], fail_silently=False)

    api_key ='EAAHyuhCkjA4BAINW0b9IjW9rkG5j7unjV5l2RYZBRFoQxymvfn7FIt47oQLnGbb71RJnrAFU2MkQtELWKndJ0YRryTZAtp6xmAEP1RkUxtz8gVXEK3ylmGkZA2d3DjkGXyaX3hshONjkag5aSM8NCfai29X8MapFcfABNZBXzArOMcc0Ynzm'
    h = requests.get(
         "https://graph.facebook.com/v15.0/me?fields=posts%7Bmessage%2Cfull_picture%2Cpermalink_url%7D&access_token="+api_key)
    json2 = h.json()


  
    return render(request,'home.html',{'json2':json2})
  
def hire(request):
     return render(request,'arena.html')

  
def livery(request):
     return render(request,'livery.html')

def contact(request):
     return render(request,'contact.html')

  
def shop(request):
     return render(request,'shop.html')
