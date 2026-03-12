from django.db import models

class ITSecialist(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    age = models.IntegerField()
    city = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    experience = models.IntegerField()
    skills = models.TextField()
    github = models.URLField()
    photo = models.ImageField(upload_to='candidates/')
    resume = models.FileField(upload_to='resumes/')
    
    def __str__(self):
        return self.full_name
