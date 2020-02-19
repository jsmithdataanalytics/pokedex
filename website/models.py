from django.db import models


class Type(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return f'Type({self.name})'


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

    def types(self):
        return [self.primary_type, self.secondary_type]

    def height_in_m(self):
        return self.height / 10.0

    def height_in_in(self):
        return self.height_in_m() / 0.0254

    def height_in_ft(self):
        return self.height_in_in() // 12, self.height_in_in() % 12

    def weight_in_kg(self):
        return self.weight / 10.0

    def weight_in_lb(self):
        return self.weight_in_kg() * 2.2

    def __str__(self):
        return f'Pokemon({self.name})'
