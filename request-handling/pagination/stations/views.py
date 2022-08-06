from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
import csv


def index(request):
    return redirect(reverse('bus_stations'))



def bus_stations(request):
    need_list = []

    with open('data-398-2018-08-30.csv', 'r', encoding='UTF-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for name in reader:
            need_list.append({'Name': name['Name'], 'Street': name['Street'], 'District': name['District']})

    page_num = int(request.GET.get("page", 1))
    paginator = Paginator(need_list, 10)
    page = paginator.get_page(page_num)
    context = {
        'bus_stations': page,
        'page': page,
    }
    return render(request, 'index.html', context)
