from dataclasses import field
from statistics import mode
from django.forms import ModelForm
from .models import PV, Tache, Membre

class PVForm(ModelForm):
    class Meta:
        model = PV
        fields = '__all__'

class TacheForm(ModelForm):
    class Meta:
        model = Tache
        fields = ['nom_tache', 'description_tache']

class MembreForm(ModelForm):
    class Meta:
        model = Membre
        fields = ['nom_membre', 'prenom_membre']