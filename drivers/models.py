from django.db import models


class DriverModel(models.Model):
    full_name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='drivers/')
    birth_date = models.DateField()
    car = models.CharField(max_length=100)
    experience = models.IntegerField()
    license = models.BooleanField(default=False)

    def __str__(self):
        return self.full_name