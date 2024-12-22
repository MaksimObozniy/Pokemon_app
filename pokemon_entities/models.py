from django.db import models  # noqa F401

# your models here

class Pokemon(models.Model):
    title = models.CharField(max_length=20)
    photo = models.ImageField()
    
    def __str__(self):
        return f"{self.title}"
    
class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    lat = models.FloatField()
    lon = models.FloatField()
    appeared_at = models.DateTimeField(null=True, blank=True)
    disappeared_at = models.DateTimeField(null=True, blank=True)
    level = models.IntegerField()
    health = models.IntegerField()
    strength = models.IntegerField()
    defence = models.IntegerField()
    stamina = models.IntegerField()
    
    def __str__(self):
        return f'{self.pokemon.title} ({self.lat}, {self.lon})'
    