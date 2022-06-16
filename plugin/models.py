from django.db import models


class Tache(models.Model):
    nom_tache = models.CharField(max_length=100)
    duree = models.DurationField()


class Utilisateur(models.Model):
    nom = models.CharField(max_length=20)
    prenom = models.CharField(max_length=50)
    tache = models.ManyToManyField(Tache)
