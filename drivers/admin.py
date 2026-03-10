from django.contrib import admin
from .models import DriverModel


@admin.register(DriverModel)
class DriverAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'full_name',
        'birth_date',
        'car',
        'experience',
        'license'
    )