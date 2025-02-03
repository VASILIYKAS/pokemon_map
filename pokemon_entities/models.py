from django.db import models  # noqa F401

# your models here


class Pokemon(models.Model):
    title_ru = models.CharField(max_length=200)
    title_en = models.CharField(max_length=200, blank=True)
    title_jp = models.CharField(max_length=200, blank=True)
    image = models.ImageField(null=True)
    description = models.TextField(null=True, blank=True)
    previous_evolution = models.ForeignKey('self',
                                       on_delete=models.SET_NULL,
                                       null=True, 
                                       blank=True,
                                       related_name='next_evolution',
                                       verbose_name='Из кого эволюционирует'
                                       )


    def __str__(self):
        return self.title_ru


class PokemonEntity(models.Model):
    name = models.ForeignKey(Pokemon, on_delete=models.CASCADE, default=1)
    lat = models.FloatField(null=True, blank=True)
    lon = models.FloatField(null=True, blank=True)
    appeared_at = models.DateTimeField(null=True, blank=True)
    disappeared_at = models.DateTimeField(null=True, blank=True)
    level = models.IntegerField(null=True, blank=True)
    health = models.IntegerField(null=True, blank=True)
    strength = models.IntegerField(null=True, blank=True)
    defence = models.IntegerField(null=True, blank=True)
    stamina = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.name}'
