from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from places.models import Place


def get_place_detail(place):
    place_detail = {
        'type': 'Feature',
        'geometry': {
            'type': 'Point',
            'coordinates': [place.lng, place.lat]
        },
        'properties': {
            'title': place.title,
            'placeId': place.id,
            'detailsUrl': reverse('place_detail', args=[place.id])
        }
    }
    return place_detail


def index(request):
    places = Place.objects.all()
    places_points = [get_place_detail(place) for place in places]
    features = {
        'type': 'FeatureCollection',
        'features': places_points,
    }
    return render(request, 'index.html', context=features)


def place_detail_view(request, place_id):
    place = get_object_or_404(Place, pk=place_id)

    place_details = {
        'title': place.title,
        'imgs': [image.image.url for image in place.images.all()],
        'description_short': place.description_short,
        'description_long': place.description_long,
        'coordinates': {
            'lng': place.lng,
            'lat': place.lat
        }
    }
    return JsonResponse(place_details,
                        json_dumps_params={'ensure_ascii': False})
