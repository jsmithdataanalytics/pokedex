# Generated by Django 3.0.3 on 2020-02-19 23:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_pokemon_evolves_to'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pokemon',
            name='evolves_to',
        ),
    ]