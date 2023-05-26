from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.db.models import Q
from django.contrib.auth.models import User
from configuration.models import competences, diplomesFormations, experiencesStages, Types

# ajouter import du modele Article ici 
def index(request):
 context = {
    'name': 'Dalel loussaief',
    'title': 'IT STUDENT',
    'bio': 'welcome',
    'Hobbies': [
        {
           'nom': 'Web Development',
           'description': '',
        },
        {
           'nom': 'Reading Books',
           'description': '',
        },
        {
           'nom': 'Writing',
           'description': '',
        }
    ],
    'SocialLife': {
        'social1':{
            'nom': 'Google Developer Student Clubs Nabeul',
            'position':'Ex-RH',
            'period':'2021-2022',
        }, 
        'social2':{
            'nom': 'Tunisia88',
            'position':'Ex-Leader',
            'period': '2019-2020',
        },
        'social3':{
            'nom': 'Tunivision ISET Nabeul',
            'position':'Ex-Membre',
            'period':'2021-2021'
        },
        'social4':{
            'nom': 'Tunisian red crescent Nabeul local committee',
            'position':'Ex-Membre',
            'period':'2018 - Present'
        },
    }
 }
 return render(request, 'infosGenerales.html', {'data':context})



def list_competences(request):
    listeCompetences = competences.objects.all().values()
    context = {
    'listeCompetences': listeCompetences,
    }
    return render(request, 'competences.html', {'data':context})



def list_diplomesEtformations(request):
    listeDiplomesFormations = diplomesFormations.objects.all().values()
    listeTypes = Types.objects.all().values()
    context = {
    'listeDiplomesFormations': listeDiplomesFormations,
    'listeTypes': listeTypes,
    }
    return render(request, 'diplomesFormations.html', {'data':context})


def list_experiencesEtStages(request):
    listeExperiencesStages = experiencesStages.objects.all().values()
    context = {
    'listeExperiencesStages': listeExperiencesStages,
    }
    return render(request, 'experiencesStages.html', {'data':context})

