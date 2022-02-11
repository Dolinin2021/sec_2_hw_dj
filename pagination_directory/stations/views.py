from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.urls import reverse
import csv


stations_list = []

with open('data-398-2018-08-30.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        stations_list.append(row)


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    paginator = Paginator(stations_list, 10)
    page_number = int(request.GET.get("page", 1))
    page = paginator.get_page(page_number)
    context = {
        'bus_stations': page.object_list,
        'page': page,
    }
    return render(request, 'stations/index.html', context)