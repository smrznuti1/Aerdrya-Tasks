from django.http import Http404, HttpResponse
from django.shortcuts import render

from .models import Number


# Create your views here.
def get_number(request, number):
    try:
        num = Number.objects.get(number=number)
    except Number.DoesNotExist:
        raise Http404("Number does not exist.")
    return render(request, "whatsapp_numbers/number_detail.html", {"number": num})
    # return HttpResponse(f"Wow, {num} is a nice number.")


def list_database(request):
    numbers = Number.objects.all()
    output = ", ".join([str(number) for number in numbers])
    context = {"numbers": numbers}
    # return HttpResponse(output)
    return render(request, "whatsapp_numbers/index.html", context)
    # return HttpResponse(render(context, request))


def welcome(request):
    return HttpResponse("Welcome.")


def submit_number(request):
    try:
        new_number = Number(int(request.POST["number"]))
    except ValueError:
        return render(
            request,
            "whatsapp_numbers/submit_number.html",
            {"error_message": "Please insert and integer."},
        )
    new_number.save()
    return render(request, "whatsapp_numbers/submit_number.html")
