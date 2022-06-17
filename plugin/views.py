from django.shortcuts import render

from .models import Utilisateur


def login_form(request):
    return render(request, 'plugin/login.html')


def creation_form(request):
    return render(request, 'plugin/nouvel_utilisateur.html')


def accueil(request):
    nom = request.POST.get('nom')
    prenom = request.POST.get('prenom')
    mot_de_passe = request.POST.get('password')

    utilisateur = Utilisateur(nom=nom, prenom=prenom, mot_de_passe=mot_de_passe)
    # utilisateur.save()

    return render(request, 'plugin/accueil.html', {'UTILISATEUR': utilisateur})


def nouvel_utilisateur(request):
    pass
