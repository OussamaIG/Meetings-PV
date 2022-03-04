from multiprocessing import context
from django.shortcuts import redirect, render
from django.db.models import Q
from .forms import PVForm, TacheForm, MembreForm
from .models import PV, Membre, Tache

# Create your views here.

def HomePage(request):

    context ={}
    return render(request, 'base/home.html', context)

def ListePV(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    pvs = PV.objects.filter(Q(nom_pv__icontains=q))


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
        return redirect('addtache')

    context ={'form' : form}
    return render(request,'base/add.html', context)

def addtache(request):
    form = TacheForm()
    pv = PV.objects.last()
    if request.method =='POST':
        form = TacheForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.PV_att = pv
            obj.save()
        return redirect('addmembre')

    context ={'form' : form}
    return render(request,'base/add.html', context)

def addmembre(request):
    form = MembreForm()
    tache = Tache.objects.last()
    pv = PV.objects.last()
    if request.method =='POST':
        form = MembreForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.tache = tache
            obj.pv_in=pv
            obj.save()
        return redirect('pvpage', pk=pv.id)

    context ={'form' : form}
    return render(request,'base/addmember.html', context)

def addmembertopv(request, pk):
    form = MembreForm()
    pv = PV.objects.get(id=pk)
    if request.method =='POST':
        form = MembreForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.pv_in = pv
            obj.save()
            return redirect('pvpage', pk=pv.id)

    context ={'form' : form}
    return render(request,'base/addmember.html', context)

def addtachetopv(request, pk):
    form = TacheForm()
    pv = PV.objects.get(id=pk)
    if request.method =='POST':
        form = TacheForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.PV_att = pv
            obj.save()
            return redirect('addmembre')

    context ={'form' : form}
    return render(request,'base/add.html', context)



#DELETING

def deletepv(request, pk):
    pv = PV.objects.get(id=pk)
    if request.method =='POST':
        pv.delete()
        return redirect('listepv')
    
    context={'pv' : pv}
    return render(request, 'base/delete.html', context)

def deletetache(request, pk):
    tache = Tache.objects.get(id = pk)
    if request.method == 'POST':
        tache.delete()
        return redirect('pvpage', pk=tache.PV_att.id)

    context = {"tache" : tache}
    return render(request,'base/delete.html', context)

def deletemember(request, pk):
    member = Membre.objects.get(id = pk)
    if request.method == 'POST':
        member.delete()
        return redirect('pvpage', pk=member.pv_in.id)

    context={'member' : member}
    return render(request, 'base/delete.html', context)


