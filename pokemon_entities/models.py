from django.db import models  # noqa F401

# your models here


class Pokemon(models.Model):
    title_ru = models.CharField(max_length=200, verbose_name='Имя на Русском')
    title_en = models.CharField(max_length=200, blank=True, verbose_name='Имя на Английском')
    title_jp = models.CharField(max_length=200, blank=True, verbose_name='Имя на Японском')
    image = models.ImageField(null=True, verbose_name='Изображение')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
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
    name = models.ForeignKey(Pokemon, on_delete=models.CASCADE, default=1, verbose_name='Имя')
    lat = models.FloatField(null=True, blank=True, verbose_name='Широта')
    lon = models.FloatField(null=True, blank=True, verbose_name='Долгота')
    appeared_at = models.DateTimeField(null=True, blank=True, verbose_name='Время появления')
    disappeared_at = models.DateTimeField(null=True, blank=True, verbose_name='Время исчезновения')
    level = models.IntegerField(null=True, blank=True, verbose_name='Уровень')
    health = models.IntegerField(null=True, blank=True, verbose_name='Здоровье')
    strength = models.IntegerField(null=True, blank=True, verbose_name='Сила')
    defence = models.IntegerField(null=True, blank=True, verbose_name='Защита')
    stamina = models.IntegerField(null=True, blank=True, verbose_name='Выносливость')

    def __str__(self):
        return f'{self.name}'
