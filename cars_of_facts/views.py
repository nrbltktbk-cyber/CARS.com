from django.shortcuts import render, get_object_or_404
from .models import Car

from django.http import HttpResponse

def car_list_view(req):
    cars = Car.objects.all()
    return render(req, 'cars_of_facts/car_list.html', {'cars': cars})

def car_detail_view(req, car_id):
    car = get_object_or_404(Car, id=car_id)
    return render(req, 'cars_of_facts/car_detail.html', {'car': car})


def bmw_fact(req):
    return HttpResponse("BMW была основана в 1916 году в Германии.")


def toyota_fact(req):
    return HttpResponse("Toyota — самый крупный автопроизводитель в мире.")


def mercedes_fact(req):
    return HttpResponse("Mercedes-Benz создал первый в мире автомобиль.")


def all_facts(req):
    return render(req, 'facts.html')

