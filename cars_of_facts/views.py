from django.shortcuts import render

from django.http import HttpResponse


def bmw_fact(req):
    return HttpResponse("BMW была основана в 1916 году в Германии.")


def toyota_fact(req):
    return HttpResponse("Toyota — самый крупный автопроизводитель в мире.")


def mercedes_fact(req):
    return HttpResponse("Mercedes-Benz создал первый в мире автомобиль.")


def all_facts(req):
    return render(req, 'facts.html')

