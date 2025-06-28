from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def get_number(request):
    return HttpResponse("This is a request for WhatsApp Number Change")
