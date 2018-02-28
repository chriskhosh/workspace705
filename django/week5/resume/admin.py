from django.contrib import admin
from .models import resume, experience, education

# Register your models here.

admin.site.register(resume)
admin.site.register(experience)
admin.site.register(education)
