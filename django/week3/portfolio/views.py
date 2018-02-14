from django.shortcuts import render

def home(request):
    '''
    Renders home page
    '''
    greeting = "My home"
    # a dictionary with a keyword 'our_greeting' mapping to the variable greeting defined above.
    context = {'our_greeting':greeting}
    return render(request, 'home.html', context)

def resume(request):
    '''
    Renders resume page
    '''
    greeting = "My resume"
    # a dictionary with a keyword 'our_greeting' mapping to the variable greeting defined above.
    context = {'our_greeting':greeting}
    return render(request, 'resume.html', context)

def portfolio(request):
    '''
    Renders portfolio page
    '''
    greeting = "My portfolio"
    # a dictionary with a keyword 'our_greeting' mapping to the variable greeting defined above.
    context = {'our_greeting':greeting}
    return render(request, 'portfolio.html', context)

def contact(request):
    '''
    Renders contact page
    '''
    greeting = "My contact"
    # a dictionary with a keyword 'our_greeting' mapping to the variable greeting defined above.
    context = {'our_greeting':greeting}
    return render(request, 'contact.html', context)