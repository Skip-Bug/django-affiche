from django.shortcuts import render

from .models import Place


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
                    "detailsUrl": "{}",
                },
            }
        )
    geojson = {"type": "FeatureCollection", "features": features}
    return render(request, "index.html", {"places_geojson": geojson})
