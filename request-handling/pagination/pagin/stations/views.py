import csv
import os
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
path = os.path.abspath('../../data-398-2018-08-30.csv')


def index(request):
    return redirect(reverse('bus_stations'))


with open(path, encoding='utf-8') as csvfile:
    content = []
    reader = csv.DictReader(csvfile)
    for name in reader:
        content.append({'Name': name['Name'], 'Street': name['Street'], 'District': name['District']})


def bus_stations(request):
    page_num = int(request.GET.get('page', 1))
    paginator = Paginator(content, 10)
    page = paginator.get_page(page_num)

    context = {
        'bus_stations': content,
        'page': page,
    }
    return render(request, 'stations/index.html', context)

