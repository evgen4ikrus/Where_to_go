from django.db import models

class Place(models.Model):
    title = models.CharField('Название', max_length=200)
    description_short = models.TextField('Краткое описание')
    description_long = models.TextField('Подробное описание')
    lng = models.FloatField('Долгота')
    lat = models.FloatField('Штрота')

    def __str__(self):
            return self.title

    class Meta:
        verbose_name = 'Место отдыха'
        verbose_name_plural = 'Места отдыха'


class Image(models.Model):
    number = models.IntegerField('Порядковый номер')
    place = models.ForeignKey(
        'Place',
        on_delete=models.CASCADE,
        verbose_name='Место оьдых',
        related_name='images'
    )
    image = models.ImageField(upload_to='images/',)

    def __str__(self):
            return f'{self.number} {self.place}'

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'
