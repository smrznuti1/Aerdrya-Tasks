from django.db import models

# Create your models here.


class Number(models.Model):
    """
    This is a number model. Simple number storage in a separate database.
    """

    number: models.IntegerField = models.IntegerField(primary_key=True)

    def __str__(self):
        return str(self.number)


class StringNumber(models.Model):
    """
    String Number, a model to store transformed numbers from the Number model.
    Primary Key is the number from Number model.
    String Number is calculated.
    """

    number: models.OneToOneField = models.OneToOneField(
        Number, models.CASCADE, primary_key=True
    )
    string_number: models.CharField = models.CharField(max_length=200)

    def __transform_digit(self, digit):
        """
        Helper function to transform a digit into it's string representation.
        """
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

    def __init__(self, number, string_number=""):
        """
        Modified init function to calculate string representation of a number.
        """
        string_number = self.transform_number(number)
        super().__init__(number, string_number)

    def save(self):
        """
        Modified save to always calculate the value of string_number.
        """
        if type(self.number) is not Number:
            self.number = Number(self.number)
        self.string_number = self.transform_number(self.number.number)
        super().save()

    def transform_number(self, number):
        """
        Transform multi-digit number into it's string representation.
        """
        digits = str(number)
        return ("-").join(
            [self.__transform_digit(string_digit) for string_digit in digits]
        )

    def __str__(self):
        return self.string_number
