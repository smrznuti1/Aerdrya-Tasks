from django.http import HttpResponse

from .models import Number

# from django.shortcuts import render


# Create your views here.
def get_number(request, number):
    return HttpResponse(f"Wow, {number} is a nice number.")


def list_database(request):
    numbers = Number.objects.all()
    output = ", ".join([str(number) for number in numbers])
    return HttpResponse(output)


def welcome(request):
    return HttpResponse("Welcome.")
