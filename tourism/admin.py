from django.contrib import admin

from django.contrib import admin
from .models import Person, Tour, Booking, Category

admin.site.register(Person)
admin.site.register(Tour)
admin.site.register(Booking)
admin.site.register(Category)
