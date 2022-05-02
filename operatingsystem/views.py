from pyexpat import model
from django.shortcuts import render
from .forms import OSForm, VersionForm
from . import models
from django.http import HttpResponseRedirect
from django.forms.models import model_to_dict

### CONTENANT

def list_os(request):
    return render(request, "os/list_os.html",{"operatingsystem" : models.operatingsystem.objects.all() })

def add_os(request):
    if request.method == "POST": 
    # arrive en cas de retour sur cette page après une saisie invalide on récupère donc les données. 
    # Normalement nous ne devrions pas passer par ce chemin la pour le traitement des données
        form = OSForm(request)
        if form.is_valid(): # validation du formulaire.
            opesys = form.save() # sauvegarde dans la base
            return list_os(request)
        else:
            return render(request,"os/add_os.html",{"form": form})
    else :
        form = OSForm() # création d'un formulaire vide
        return render(request,"os/add_os.html",{"form" : form})

def save_os(request):
    osform = OSForm(request.POST)
    if osform.is_valid():
        opesys = osform.save()
        return list_os(request)
    else:
        return render(request,"os/add_os.html",{"form": osform})

def details(request, id):
    return render(request,"os/details.html",{"operatingsystem" : models.operatingsystem.objects.get(pk=id)})

def delete_os(request, id):
    models.operatingsystem.objects.filter(id=id).delete()
    return HttpResponseRedirect("/os/list")

def edit_os(request, id):
    opesys = models.operatingsystem.objects.get(pk=id)
    osform = OSForm(model_to_dict(opesys))
    print(osform)
    if request.method == "POST": 
        form = OSForm(request)
        if form.is_valid(): # validation du formulaire.
            opesys = form.save() # sauvegarde dans la base
            return render(request,"os/details.html",{"operatingsystem" : opesys}) # envoie vers une page d'affichage du livre créé
        else:
            return render(request,"os/add_os.html",{"form": form})
    else :
        return render(request, "os/edit_os.html", {"form": osform,"id":id})


def save_edit_os(request, id):
    osform = OSForm(request.POST)
    if osform.is_valid():
        opesys = osform.save(commit=False)
        opesys.id = id;
        opesys.save()
        return list_os(request)
    else:
        return render(request, "os/edit_os.html", {"form": osform, "id": id})


### CONTENU
def list_ver(request):
    return render(request, "ver/list.html",{"versions" : models.versions.objects.all()})

def add_ver(request):
    if request.method == "POST": 
    # arrive en cas de retour sur cette page après une saisie invalide on récupère donc les données. 
    # Normalement nous ne devrions pas passer par ce chemin la pour le traitement des données
        form = VersionForm(request)
        if form.is_valid(): # validation du formulaire.
            ver = form.save() # sauvegarde dans la base
            return list_os(request)
        else:
            return render(request,"ver/add.html",{"form": form})
    else :
        form = VersionForm() # création d'un formulaire vide
        return render(request,"ver/add.html",{"form" : form})
