from django.contrib import admin

from .models import Number, StringNumber

# Register your models here.
admin.site.register(Number)
admin.site.register(StringNumber)
