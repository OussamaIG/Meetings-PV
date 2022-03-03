from multiprocessing import context
from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import PV, Tache, Membre
from .serializers import PVSerializer, MembreSerializer, TacheSerializer

@api_view(['GET'])
def Liste_of_pv(request):
    pvs = PV.objects.all()
    serializer = PVSerializer(pvs, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def Liste_of_membres(request):
    membres = Membre.objects.all()
    serializer = MembreSerializer(membres, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def Liste_of_taches(request):
    taches = Tache.objects.all()
    serializer = TacheSerializer(taches, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def addPV(request):
    serializer = PVSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def addMembre(request):
    serializer = MembreSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def addTache(request):
    serializer = TacheSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

