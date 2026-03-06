from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tour(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    categories = models.ManyToManyField(Category, related_name='tours')

    def __str__(self):
        return self.title


class Booking(models.Model):
    person = models.OneToOneField(
        Person,
        on_delete=models.CASCADE
    )

    tour = models.ForeignKey(
        Tour,
        on_delete=models.CASCADE
    )

    booking_date = models.DateTimeField()

    def __str__(self):
        return f"{self.person} - {self.tour}"


class Review(models.Model):
    person = models.ForeignKey(
        Person,
        on_delete=models.CASCADE
    )

    tour = models.ForeignKey(
        Tour,
        on_delete=models.CASCADE,
        related_name='reviews'
    )

    comment = models.TextField()
    rating = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Отзыв от {self.person}"