from dataclasses import field
from rest_framework import serializers
from base.models import PV, Tache, Membre


class PVSerializer(serializers.ModelSerializer):
    class Meta:
        model = PV
        fields = '__all__'

class MembreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Membre
        fields = '__all__'

class TacheSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tache
        fields = '__all__'