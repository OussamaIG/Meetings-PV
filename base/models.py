from statistics import mode
from django.db import models

# Create your models here.

class Membre(models.Model):
    nom_membre = models.CharField(max_length=50)
    prenom_membre = models.CharField(max_length=50)

    def __str__(self):
        return self.nom_membre+self.prenom_membre


class Tache(models.Model):
    nom_tache = models.CharField(max_length=100)
    description_tache = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nom_tache

class PV(models.Model):
    nom_pv = models.CharField(max_length=80)
    but_pv = models.TextField(null=True, blank=True)
    point_abordes_pv = models.TextField(null=True, blank=True)
    decision_prise_pv = models.TextField(null=True, blank=True)
    date_pv = models.DateField()
    h_debut_pv = models.TimeField()
    h_fin_pv = models.TimeField()

