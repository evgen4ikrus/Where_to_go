from django.core.management.base import BaseCommand
import requests
from places.models import Place, Image
from urllib.parse import urlparse
from django.core.files.base import ContentFile


class Command(BaseCommand):
    help = 'Load new place'    

    def handle(self, *args, **options):
        
        json_url = options['json_url']
        response = requests.get(json_url)
        response.raise_for_status()
        place_raw = response.json()

        place, created = Place.objects.get_or_create(
            title=place_raw['title'],
            defaults = {
                'description_short': place_raw['description_short'],
                'description_long': place_raw['description_long'],
                'lat': place_raw['coordinates']['lat'],
                'lng': place_raw['coordinates']['lng'],
            }
        )

        for number, img_url in enumerate(place_raw['imgs']):
            place_img = Image.objects.create(number=number, place=place)
            name = urlparse(img_url).path.split('/')[-1]

            response = requests.get(img_url)
            response.raise_for_status()
            image_content = ContentFile(response.content)

            place_img.image.save(name, image_content, save=True)

    def add_arguments(self, parser):
        parser.add_argument('json_url', type=str)
