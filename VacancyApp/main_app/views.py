import re
import requests
from datetime import datetime

from django.shortcuts import render

from vacancy.service import *
from models import *
from vacancy.api import ApiHeadHunter


def home_page(request):
    return render(request, 'HomePage.html',
                  {'context': Main.objects.all()})


def demand_page(request):
    return render(request, 'base.html', {'context': Info.objects.all()})


def geography_page(request):
    return render(request, 'Geography.html',
                  {'context': Location.objects.all()})


def skills_page(request):
    return render(request, 'Skills.html', {'context': Ability.objects.all()})


def last_vacancy_page(request):
    for vacancy in last_vacancies:
        name_vacancy_to_parse = vacancy.name_vacancy_to_parse
    hh = ApiHeadHunter(name_vacancy_to_parse)
    vacs = hh.get_data_vacancies(datetime.now().strftime('%Y-%m-%d'), 10)

    context = {'vacs': vacs}

    return render(request, 'LastVacancy.html', context)
