from django.http import HttpResponse
from django.shortcuts import render


def __transform_number(number):
    digits = str(number)
    return (" ").join([__transform_digit(string_digit) for string_digit in digits])


def __transform_digit(digit):
    match digit:
        case "0":
            return "zero"
        case "1":
            return "one"
        case "2":
            return "two"
        case "3":
            return "three"
        case "4":
            return "four"
        case "5":
            return "five"
        case "6":
            return "six"
        case "7":
            return "seven"
        case "8":
            return "eight"
        case "9":
            return "nine"


# Create your views here.
def get_number(request):
    number = 43424
    string_number = __transform_number(43424)
    return HttpResponse(f"This is your number: {string_number}")
