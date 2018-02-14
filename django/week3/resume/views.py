from django.shortcuts import render
from .models import education, experience

# Create your views here.

def home(request):
    qs = education.objects.order_by('-title')
    context = { 'educations': qs}
    return render(request, 'resume/home.html', context)