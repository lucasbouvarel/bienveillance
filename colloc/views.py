# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from colloc.forms import ConnexionForm
from django.urls import reverse
from colloc.models import Person, Transaction
from django.shortcuts import redirect
from django.utils import timezone

# Create your views here.
def connexion(request):
    error = False
    next=request.GET.get('next')
    if not next:
        next='/home'
    else:
        next=request.GET['next']
    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)  # Nous vérifions si les données sont correctes
            if user:  # Si l'objet renvoyé n'est pas None
                login(request, user)  # nous connectons l'utilisateur
            else: # sinon une erreur sera affichée
                error = True
    else:
        form = ConnexionForm()

    return render(request, 'connexion.html', locals())


def vote(request):
    person=Person.objects.all().order_by('-date')
    transactions=Transaction.objects.all()




    return render(request,"liste.html",locals())

@login_required
def voteid(request,id):
    person=Person.objects.get(user=id)

    if request.method == "POST":

        if(person.user==request.user):
            mauvais=True
            person.vote=person.vote-20
            person.save()
            trans=Transaction(collocDonneur=Person.objects.get(user=request.user.id), collocReceveur=person,raison="triche, essaye de se donner des points",point=-20)
            trans.save();
        else:
            nombre=request.POST['nombre']
            print(nombre)
            print(person.vote)
            person.vote=person.vote+int(nombre)
            print(person.vote)
            person.save()
            trans=Transaction(collocDonneur=Person.objects.get(user=request.user.id), collocReceveur=person,raison=request.POST["raison"],point=nombre)
            trans.save();

            transactions=Transaction.objects.all()

            classement=Person.objects.all()
            return redirect("/colloc/vote",locals())

    return render(request,"vote.html",locals())
