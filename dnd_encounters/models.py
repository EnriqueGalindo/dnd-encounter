from django.db import models


class Post(models.Model):
    name = models.CharField(max_length=30)
    hit_points = models.IntegerField()
    armor_class = models.IntegerField()
    resistances = models.CharField(max_length=280)
    immunities = models.CharField(max_length=280)
    speed = models.IntegerField()
