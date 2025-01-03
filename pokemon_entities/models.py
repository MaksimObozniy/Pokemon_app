from django.db import models  # noqa F401


class Pokemon(models.Model):
    title_ru = models.CharField(
        max_length=20,
        verbose_name='Название на русском'
        )
    
    title_en = models.CharField(
        max_length=20, 
        blank=True,
        null=True,
        verbose_name='Название на английском'
        )
    
    title_jp = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        verbose_name='Название на японском'
        )
    
    photo = models.ImageField(
        verbose_name='Фотография'
    )
    
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name='Описание'
        )
    
    previous_evolution = models.ForeignKey(
        "self",
        verbose_name='Из кого эволюционирует',
        on_delete=models.SET_NULL,
        null=True,
        related_name='next_evolutions',
        blank=True
    )
    
    def __str__(self):
        return self.title_ru
    
class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(
        Pokemon,
        on_delete=models.SET_NULL,
        verbose_name='Покемон',
        related_name="entities",
        null=True,
        blank=True
    )
    
    lat = models.FloatField(
        verbose_name='Широта'
    )
    
    lon = models.FloatField(
        verbose_name='Долгота'
    )
    
    appeared_at = models.DateTimeField(
        null=True, 
        blank=True,
        verbose_name='Появился в'
        )
    
    disappeared_at = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name='Исчез в'
        )
    
    level = models.IntegerField(
        null=True, 
        blank=True,
        verbose_name='Уровень'
    )
    
    health = models.IntegerField(
        null=True, 
        blank=True,
        verbose_name='Здоровье'
    )
    
    strength = models.IntegerField(
        null=True, 
        blank=True,
        verbose_name='Здоровье'
    )
    
    defence = models.IntegerField(
        null=True, 
        blank=True,
        verbose_name='Защита'
    )
    
    stamina = models.IntegerField(
        null=True, 
        blank=True,
        verbose_name='Выносливость'
    )
    
    def __str__(self):
        return f'{self.pokemon.title_ru} ({self.lat}, {self.lon})'
    
