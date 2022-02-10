from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.urls import reverse
import csv


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):

    stations_list = []

    with open('data-398-2018-08-30.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            stations_list.append(row)

    paginator = Paginator(stations_list, 10)
    page_number = int(request.GET.get("page", 1))
    context = {
        'bus_stations': paginator.get_page(page_number),
        'page': paginator.page(page_number),
    }

    return render(request, 'stations/index.html', context)