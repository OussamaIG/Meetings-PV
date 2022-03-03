from statistics import mode
from django.db import models

# Create your models here.

class PV(models.Model):
    nom_pv = models.CharField(max_length=80)
    but_pv = models.TextField(null=True, blank=True)
    point_abordes_pv = models.TextField(null=True, blank=True)
    decision_prise_pv = models.TextField(null=True, blank=True)
    date_pv = models.DateField()
    h_debut_pv = models.TimeField()
    h_fin_pv = models.TimeField()


    def __str__(self):
        return self.nom_pv

    class Meta:
        ordering = ['-date_pv']
    

class Tache(models.Model):
    nom_tache = models.CharField(max_length=100)
    description_tache = models.TextField(null=True, blank=True)
    PV_att = models.ForeignKey(PV,on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.nom_tache

class Membre(models.Model):
    nom_membre = models.CharField(max_length=50)
    prenom_membre = models.CharField(max_length=50)
    tache = models.ForeignKey(Tache,on_delete=models.CASCADE, null=True)
    pv_in = models.ForeignKey(PV,on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.nom_membre+self.prenom_membre


