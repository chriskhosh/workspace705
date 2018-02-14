from django.db import models

# Create your models here.

class experience(models.Model):
    title = models.TextField(max_length=255)
    location = models.TextField(max_length=255)
    start_date = models.DateField(max_length=255)
    end_date = models.DateField(max_length=255)
    description = models.TextField(max_length=255)

class education(models.Model):
    institution_name = models.TextField(max_length=255)
    location = models.TextField(max_length=255)
    degree = models.TextField(max_length=255)
    major = models.TextField(max_length=255)
    gpa = models.FloatField(max_length=255)