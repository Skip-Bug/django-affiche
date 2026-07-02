from django.urls import path

from . import views

urlpatterns = [
    path("", views.start_page, name="home"),
    path("places/<int:place_id>/", views.place_desc, name="place_desc"),
]
