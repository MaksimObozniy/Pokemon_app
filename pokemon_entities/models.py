from django.db import models  # noqa F401

# your models here

class Pokemon(models.Model):
    title = models.CharField(max_length=20)
    title_en = models.CharField(max_length=20, blank=True)
    title_jp = models.CharField(max_length=20, blank=True)
    photo = models.ImageField()
    description = models.TextField(blank=True)
    previous_evolution = models.ForeignKey(
        "self",
        verbose_name='Из кого эволюционирует',
        on_delete=models.SET_NULL,
        null=True,
        related_name='next_evolutions',
        blank=True
    )
    
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
    