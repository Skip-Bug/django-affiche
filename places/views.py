from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Place


def place_desc(request, place_id):
    place = get_object_or_404(
        Place.objects.prefetch_related("images"),
        id=place_id,
    )
    images = place.images.all().order_by("order")

    descriptions = {
        "title": place.title,
        "imgs": [img.image.url for img in images],
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": {"lat": place.lat, "lng": place.lng},
    }

    return JsonResponse(descriptions, json_dumps_params={"ensure_ascii": False})


def start_page(request):
    places = Place.objects.all()
    features = []
    for place in places:
        features.append(
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [place.lng, place.lat],
                },
                "properties": {
                    "title": place.title,
                    "placeId": place.id,
                    "detailsUrl": reverse("place_desc", args=[place.id]),
                },
            }
        )
    geojson = {"type": "FeatureCollection", "features": features}
    return render(request, "index.html", {"places_geojson": geojson})
