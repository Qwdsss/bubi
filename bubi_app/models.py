from django.db import models


class StarWarsCharacter(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=50, null=True, blank=True)
    affiliation = models.CharField(max_length=50, null=True, blank=True)
    homeworld = models.CharField(max_length=50, null=True, blank=True)
    jedi = models.BooleanField(default=False)
    sith = models.BooleanField(default=False)