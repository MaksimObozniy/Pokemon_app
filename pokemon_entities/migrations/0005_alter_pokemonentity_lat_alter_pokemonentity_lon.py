# Generated by Django 5.1.4 on 2024-12-22 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0004_remove_pokemonentity_lat_remove_pokemonentity_lon_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemonentity',
            name='lat',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='lon',
            field=models.FloatField(),
        ),
    ]