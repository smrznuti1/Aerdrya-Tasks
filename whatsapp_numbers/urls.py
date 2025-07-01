from django.urls import path

from . import views

app_name = "numbers_app"

urlpatterns = [
    path("", views.welcome, name="welcome"),
    path("<int:number>/", views.get_number, name="get_number"),
    path("database", views.list_database, name="list_database"),
    path("submit_number", views.submit_number, name="submit_number"),
    path(
        "transform_number/<int:number>", views.transform_number, name="transform_number"
    ),
    path(
        "transform_numbers",
        views.transform_numbers_from_database,
        name="transform_numbers",
    ),
]
