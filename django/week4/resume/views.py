from django.shortcuts import render
from .models import resume, education, experience

# Create your views here.

def home(request):
    myResume = resume.objects.first()
    context = { 'myResume': myResume}
    return render(request, 'resume/home.html', context)