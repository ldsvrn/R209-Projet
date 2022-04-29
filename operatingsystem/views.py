from pyexpat import model
from django.shortcuts import render
from .forms import OSForm
from . import models
from django.http import HttpResponseRedirect
from django.forms.models import model_to_dict


def list_os(request):
    return render(request, "os/show_os.html",{"operatingsystem" : models.operatingsystem.objects.all() })

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

"""
def ajout(request):
    if request.method == "POST": 
    # arrive en cas de retour sur cette page après une saisie invalide on récupère donc les données. 
    # Normalement nous ne devrions pas passer par ce chemin la pour le traitement des données
        form = LivreForm(request)
        if form.is_valid(): # validation du formulaire.
            livre = form.save() # sauvegarde dans la base
            return render(request,"affiche.html",{"livre" : livre}) # envoie vers une page d'affichage du livre créé
        else:
            return render(request,"ajout.html",{"form": form})
    else :
        form = LivreForm() # création d'un formulaire vide
        return render(request,"ajout.html",{"form" : form})

def traitement(request):
    lform = LivreForm(request.POST)
    if lform.is_valid():
        livre = lform.save()
        return render(request,"affiche.html",{"livre" : livre})
    else:
        return render(request,"ajout.html",{"form": lform})

def show(request):
    return render(request,"show.html",{"Livre" : models.Livre.objects.all() })

def read(request, id):
    return render(request,"read.html",{"livre" : models.Livre.objects.get(pk=id)})


def update(request, id):
    livre = models.Livre.objects.get(pk=id)
    lform = LivreForm(model_to_dict(livre))
    print(lform)
    if request.method == "POST": 
        form = LivreForm(request)
        if form.is_valid(): # validation du formulaire.
            livre = form.save() # sauvegarde dans la base
            return render(request,"affiche.html",{"livre" : livre}) # envoie vers une page d'affichage du livre créé
        else:
            return render(request,"ajout.html",{"form": form})
    else :
        return render(request, "update.html", {"form": lform,"id":id})


def updatedb(request, id):
    lform = LivreForm(request.POST)
    if lform.is_valid():
        livre = lform.save(commit=False)
        livre.id = id;
        livre.save()
        return HttpResponseRedirect("/crud/show/")
    else:
        return render(request, "update.html", {"form": lform, "id": id})
"""