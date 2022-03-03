from multiprocessing import context
from django.shortcuts import redirect, render
from .forms import PVForm, TacheForm, MembreForm
from .models import PV, Membre, Tache

# Create your views here.

def HomePage(request):

    context ={}
    return render(request, 'base/home.html', context)

def CreationPage(request):

    context ={}
    return render(request, 'base/creation.html', context)

def ListePV(request):
    pvs = PV.objects.all()

    context ={'pvs': pvs}
    return render(request, 'base/listepv.html', context)

def PVpage(request, pk):
    pv = PV.objects.get(id=pk)
    taches = pv.tache_set.all()
    membres = pv.membre_set.all()
    
    context ={'pv': pv, "taches" : taches, "membres" : membres}
    return render(request, 'base/pvpage.html', context)


#INSERTING

def addPV(request):
    form = PVForm()
    if request.method =='POST':
        form = PVForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('homepage')

    context ={'form' : form}
    return render(request,'base/add.html', context)

def addtache(request):
    form = TacheForm()
    if request.method =='POST':
        form = TacheForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('homepage')

    context ={'form' : form}
    return render(request,'base/add.html', context)

def addmembre(request):
    form = MembreForm()
    if request.method =='POST':
        form = MembreForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('homepage')

    context ={'form' : form}
    return render(request,'base/add.html', context)

#DELETING

def deletetache(request, pk):
    tache = Tache.objects.get(id = pk)
    if request.method == 'POST':
        tache.delete()
        return redirect('pvpage', pk=tache.PV_att.id)

    context = {"tache" : tache}
    return render(request,'base/delete.html', context)


