from django.shortcuts import render

# Create your views here.

#landing page views
def landing(request):
    return render(request, 'landing/landing.html',)
