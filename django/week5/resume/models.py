from django.db import models

# Create your models here.

class resume(models.Model):
    first_name = models.TextField(max_length=255)
    last_name = models.TextField(max_length=255)

    def __str__(self):
        return(self.first_name)

    def get_full_name(self):
        full_name = (self.first_name + " " + self.last_name)
        return(full_name)

    def get_last_name_first_name(self):
        full_name = (self.last_name + ", " + self.first_name)
        return(full_name)

    def get_experience(self):
        return self.experience_set.all()

    def get_education(self):
        return self.education_set.all()


class experience(models.Model):
    title = models.TextField(max_length=255)
    location = models.TextField(max_length=255)
    start_date = models.DateField(max_length=255)
    end_date = models.DateField(max_length=255)
    description = models.TextField(max_length=255)
    full_name = models.ForeignKey(resume, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return(self.title)

class education(models.Model):
    institution_name = models.TextField(max_length=255)
    location = models.TextField(max_length=255)
    degree = models.TextField(max_length=255)
    major = models.TextField(max_length=255)
    gpa = models.FloatField(max_length=255)
    full_name = models.ForeignKey(resume, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return(self.institution_name)