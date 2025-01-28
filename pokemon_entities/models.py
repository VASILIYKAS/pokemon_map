from django.db import models  # noqa F401

# your models here
class Pokemon(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(null=True)

    def __str__(self):
        return self.title
    
class PokemonEntity(models.Model):
    name = models.ForeignKey(Pokemon, on_delete=models.CASCADE, default=1)
    lat = models.FloatField(null=True)
    lon = models.FloatField(null=True)

    def __str__(self):
        return f'{self}:' 

