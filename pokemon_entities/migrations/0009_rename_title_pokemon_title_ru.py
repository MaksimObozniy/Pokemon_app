# Generated by Django 5.1.4 on 2024-12-27 15:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0008_alter_pokemon_previous_evolution'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pokemon',
            old_name='title',
            new_name='title_ru',
        ),
    ]