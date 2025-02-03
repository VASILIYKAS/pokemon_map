from django.db import models  # noqa F401

# your models here


class Pokemon(models.Model):
    title_ru = models.CharField(max_length=200, verbose_name='Имя на Русском')
    title_en = models.CharField(max_length=200, blank=True, verbose_name='Имя на Английском')
    title_jp = models.CharField(max_length=200, blank=True, verbose_name='Имя на Японском')
    image = models.ImageField(upload_to='images/', default='images/default.png', verbose_name='Изображение')
    description = models.TextField(blank=True, verbose_name='Описание', default='Нет описания')
    previous_evolution = models.ForeignKey('self',
                                       on_delete=models.SET_NULL,
                                       null=True, 
                                       blank=True,
                                       related_name='next_evolution',
                                       verbose_name='Из кого эволюционирует',
                                       )


    def __str__(self):
        return self.title_ru


class PokemonEntity(models.Model):
    name = models.ForeignKey(Pokemon, on_delete=models.CASCADE, default=1, verbose_name='Имя')
    lat = models.FloatField(verbose_name='Широта', null=False)
    lon = models.FloatField(verbose_name='Долгота', null=False)
    appeared_at = models.DateTimeField(verbose_name='Время появления', null=False)
    disappeared_at = models.DateTimeField(verbose_name='Время исчезновения', null=False)
    level = models.IntegerField(null=True, blank=True, verbose_name='Уровень')
    health = models.IntegerField(null=True, blank=True, verbose_name='Здоровье')
    strength = models.IntegerField(null=True, blank=True, verbose_name='Сила')
    defence = models.IntegerField(null=True, blank=True, verbose_name='Защита')
    stamina = models.IntegerField(null=True, blank=True, verbose_name='Выносливость')

    def __str__(self):
        return f'{self.name}'
