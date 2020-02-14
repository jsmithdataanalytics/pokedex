from django.db import models


class Type(models.Model):
    name = models.CharField(max_length=10)


class Pokemon(models.Model):
    number = models.IntegerField(unique=True)
    name = models.CharField(max_length=15, unique=True)
    primary_type = models.ForeignKey(Type, related_name='primary', on_delete=models.CASCADE)
    secondary_type = models.ForeignKey(Type, related_name='secondary', on_delete=models.CASCADE, null=True, blank=True)
    height = models.IntegerField()
    weight = models.IntegerField()
    genus = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    image = models.CharField(max_length=10, unique=True)
    hp = models.IntegerField()
    attack = models.IntegerField()
    defense = models.IntegerField()
    special = models.IntegerField()
    speed = models.IntegerField()
