#-*- coding: utf-8 -*-
from django.http import HttpResponse,Http404
from datetime import datetime
from django.shortcuts import render

def home(request):
  text = """<h1>Bienvenue sur mon blog !</h1>
            <p>Les crêpes bretonnes ça tue des mouettes en plein vol !</p>"""
  return HttpResponse(text)

def view_article(request, id_article):
    """ Vue qui affiche un article selon son identifiant (ou ID, ici un numéro). Son ID est le second paramètre de la fonction
        (pour rappel, le premier paramètre est TOUJOURS la requête de l'utilisateur) """
    
    if int(id_article) > 100: #Si l'ID est supérieur à 100, nous considérons que l'article n'existe pas
        raise Http404
    text = "Vous avez demandé l'article n°{0} !".format(id_article)
    return HttpResponse(text)

def list_articles(request, month, year):
    """ Liste des articles d'un mois précis. """
 
    text = "Vous avez demandé les articles de {0} {1}.".format(month, year)
    return HttpResponse(text)

def tpl(request):
    return render(request, 'blog/tpl.html', {'current_date': datetime.now()})

def addition(request, nombre1, nombre2):   
    total = int(nombre1) + int(nombre2)
 
    # retourne nombre1, nombre2 et la somme des deux
    return render(request, 'blog/addition.html', locals())  
