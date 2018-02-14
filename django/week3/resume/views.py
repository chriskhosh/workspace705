from django.shortcuts import render
from .models import education, experience

# Create your views here.

def home(request):
    qs = education.objects.order_by('-institution_name')
    context = { 'educations': qs}
    return render(request, 'resume/home.html', context)