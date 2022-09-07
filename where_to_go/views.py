from urllib import request
from django.shortcuts import render
from places.models import Place, Image


def index(request):
    places = Place.objects.all()
    places_points = []

    for place in places:
        places_points.append(
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [place.lng, place.lat]
                },
                "properties": {
                    "title": place.title,
                    "placeId": place.id,
                    "detailsUrl": "../static/places/moscow_legends.json"
                }
            }
        )

    features = {
        "type": "FeatureCollection",
        "features": places_points,
    }

    return render(request, 'index.html', context=features)