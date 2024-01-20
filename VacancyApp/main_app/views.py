import re
import requests
from datetime import datetime

from django.shortcuts import render

from .models import *
from main_app.api.head_hunter.v1 import HeadHunter


def home_page(request):
    return render(request, 'index.html',
                  {'context': Main.objects.all()})


def demand_page(request):
    return render(request, 'info.html', {'context': Info.objects.all()})


def geography_page(request):
    return render(request, 'location.html',
                  {'context': Location.objects.all()})


def skills_page(request):
    return render(request, 'abilityes.html', {'context': Ability.objects.all()})


def last_vacancy_page(request):
    hh = HeadHunter('frontend')
    vacs = hh.get_data_vacancies('2024-01-15', 10)

    context = {'vacs': vacs}

    return render(request, 'last_vacancy.html', context)
