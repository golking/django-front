from django.urls import path
from .views import *

urlpatterns = [
    path('', home_page, name='main'),
    path('relevance', demand_page, name='relevance'),
    path('location', geography_page, name='location'),
    path('abilities', skills_page, name='abilities'),
    path('hh', last_vacancy_page, name='hh'),
]
