from django.db import models

# Create your models here.


class Number(models.Model):
    number: models.IntegerField = models.IntegerField(primary_key=True)

    def __str__(self):
        return str(self.number)


class StringNumber(models.Model):
    string_number: models.CharField = models.CharField(max_length=200)
    number: models.ForeignKey = models.ForeignKey(Number, models.CASCADE)

    def __transform_digit(self, digit):
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

    def transform_number(self, number):
        digits = str(number)
        return ("-").join(
            [self.__transform_digit(string_digit) for string_digit in digits]
        )

    def __str__(self):
        return self.string_number
