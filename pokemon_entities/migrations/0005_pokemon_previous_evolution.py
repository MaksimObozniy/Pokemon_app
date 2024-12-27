# Generated by Django 5.1.4 on 2024-12-27 14:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0004_pokemon_title_en_pokemon_title_jp'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='previous_evolution',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='next_evolutions', to='pokemon_entities.pokemon', verbose_name='Из кого эволюционирует'),
        ),
    ]
