from email.mime import image
from urllib.parse import urlparse

import requests
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand

from places.models import Image, Place


class Command(BaseCommand):
    help = 'Load new place'

    def handle(self, *args, **options):

        json_url = options['json_url']
        response = requests.get(json_url)
        response.raise_for_status()
        place_raw = response.json()

        place, created = Place.objects.get_or_create(
            title=place_raw['title'],
            defaults={
                'description_short': place_raw.get('description_short', ''),
                'description_long': place_raw.get('description_long', ''),
                'lat': place_raw['coordinates']['lat'],
                'lng': place_raw['coordinates']['lng'],
            }
        )

        for number, img_url in enumerate(place_raw['imgs']):
            response = requests.get(img_url)
            response.raise_for_status()
            name = urlparse(img_url).path.split('/')[-1]
            image_content = ContentFile(response.content, name=name)
            Image.objects.create(number=number,
                                 place=place, image=image_content)

    def add_arguments(self, parser):
        parser.add_argument('json_url', type=str)
