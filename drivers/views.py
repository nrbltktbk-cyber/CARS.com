from django.shortcuts import render, redirect, get_object_or_404
from .models import DriverModel
from .forms import DriverForm

def create_driver(request):
    if request.method == 'POST':
        form = DriverForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('drivers_list')
    else:
        form = DriverForm()

    return render(request, 'create_driver.html', {'form': form})



def driver_list(request):
    drivers = DriverModel.objects.all()
    return render(request, 'drivers_list.html', {'drivers': drivers})

def update_driver(request, id):
    driver = get_object_or_404(DriverModel, id=id)

    if request.method == 'POST':
        form = DriverForm(request.POST, request.FILES, instance=driver)
        if form.is_valid():
            form.save()
            return redirect('driver_list')
    else:
        form = DriverForm(instance=driver)

    return render(request, 'create_driver.html', {'form': form})


def delete_driver(request, id):
    driver = get_object_or_404(DriverModel, id=id)
    driver.delete()
    return redirect('drivers_list')