from django.http import Http404, HttpResponse
from django.shortcuts import render

from .models import Number, StringNumber


# Create your views here.
def get_number(request, number):
    """
    Test Function to check if number exists in the table.

    """
    try:
        num = Number.objects.get(number=number)
    except Number.DoesNotExist:
        raise Http404("Number does not exist.")
    return render(request, "whatsapp_numbers/number_detail.html", {"number": num})


def list_database(request):
    """
    List all numbers from the Model Number.
    """
    numbers = Number.objects.all()
    output = ", ".join([str(number) for number in numbers])
    context = {"numbers": numbers}
    return render(request, "whatsapp_numbers/index.html", context)


def welcome(request):
    """
    Welcome page
    """
    return HttpResponse("Welcome.")


def submit_number(request):
    """
    Submit a number to database.
    """
    if request.method == "POST":
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
    else:
        return render(request, "whatsapp_numbers/submit_number.html")


def transform_number(request, number):
    """
    Transform a single number.
    Helper view.
    """
    string_number = StringNumber(number=number)
    string_number.save()
    return HttpResponse(f"The number {string_number} is saved")


def transform_numbers_from_database(request):
    """
    Choose a number from model Number to transform and store into model StringNumber.
    """
    numbers = Number.objects.all()
    context = {"numbers": numbers}
    return render(
        request, "whatsapp_numbers/transform_numbers_from_database.html", context
    )
