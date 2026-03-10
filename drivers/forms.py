from django.forms import ModelForm
from .models import DriverModel


class DriverForm(ModelForm):
    class Meta:
        model = DriverModel
        fields = '__all__'