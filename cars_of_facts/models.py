from django.db import models

class Car(models.Model):
    title = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    year = models.IntegerField()
    engine = models.CharField(max_length=100)
    horsepower = models.IntegerField()
    color = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    mileage = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='cars/')

    def __str__(self):
        return self.title