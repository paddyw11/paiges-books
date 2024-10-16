from django.shortcuts import render

# Create your views here.

def index(request):
    """ A view to return the index page """
    
    return render(request, 'home/index.html')

def about_us(request):
    """ A view to return the About Us page """
    return render(request, 'home/about.html')

def faqs(request):
    """ A view to return the FAQs page """
    return render(request, 'home/faqs.html')
