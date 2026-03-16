from django.shortcuts import render, get_object_or_404
from .models import Car
from django.core.paginator import Paginator
from django.http import HttpResponse


def car_list(request):
    query = request.GET.get('q')

    if query:
        cars = Car.objects.filter(name__icontains=query)
    else:
        cars = Car.objects.all()

    paginator = Paginator(cars, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'car_list.html', {'page_obj': page_obj})


def car_detail(request, car_id):
    car = get_object_or_404(Car, id=car_id)

    car.views += 1
    car.save()

    return render(request, 'car_detail.html', {'car': car})


def bmw_fact(req):
    return HttpResponse("BMW была основана в 1916 году в Германии.")


def toyota_fact(req):
    return HttpResponse("Toyota — самый крупный автопроизводитель в мире.")


def mercedes_fact(req):
    return HttpResponse("Mercedes-Benz создал первый в мире автомобиль.")


def all_facts(req):
    return render(req, 'facts.html')