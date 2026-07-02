from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Place


def place_desc(request, place_id):
    place = get_object_or_404(Place, id=place_id)
    return HttpResponse(place.title)


def start_page(request):
    places = Place.objects.all()
    features = []
    for place in places:
        features.append(
            {
                "type": "Feature",
                "geometry": {"type": "Point", "coordinates": [place.lng, place.lat]},
                "properties": {
                    "title": place.title,
                    "placeId": place.id,
                    "detailsUrl": f"/places/{place.id}/",
                },
            }
        )
    geojson = {"type": "FeatureCollection", "features": features}
    return render(request, "index.html", {"places_geojson": geojson})
