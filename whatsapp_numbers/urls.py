from django.urls import path

from . import views

app_name = "numbers_app"

urlpatterns = [
    path("", views.welcome, name="welcome"),
    path("<int:number>/", views.get_number, name="get_number"),
    path("database", views.list_database, name="list_database"),
    path("submit_number", views.submit_number, name="submit_number"),
]
