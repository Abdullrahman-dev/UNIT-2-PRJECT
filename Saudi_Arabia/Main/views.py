from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
# Create your views here.

def home(request):
    theme = request.COOKIES.get('theme', 'light')
    return render(request, 'Main/home.html', {'theme': theme})

def economy_view(request):
    theme = request.COOKIES.get('theme', 'light')
    return render(request, 'Main/economy_view.html', {'theme': theme})

def sustainability_view(request):
    theme = request.COOKIES.get('theme', 'light')
    return render(request, 'Main/sustainability_view.html', {'theme': theme})

def neom_view(request):
    theme = request.COOKIES.get('theme', 'light')
    return render(request, 'Main/neom.html', {'theme': theme})

def the_line_view(request):
    theme = request.COOKIES.get('theme', 'light')
    return render(request, 'Main/the_line.html', {'theme': theme})

def the_red_sea_view(request):
    theme = request.COOKIES.get('theme', 'light')
    return render(request, 'Main/the_red_sea.html', {'theme': theme})

def innovation_technology_view(request):
    theme = request.COOKIES.get('theme', 'light')
    return render(request, 'Main/innovation_technology_view.html', {'theme': theme})

def toggle_theme(request):
    response = redirect(request.META.get('HTTP_REFERER', 'home'))
    current_theme = request.COOKIES.get('theme', 'light')
    new_theme = 'dark' if current_theme == 'light' else 'light'
    response.set_cookie('theme', new_theme, max_age=3600 * 24 * 30)
    return response

def about_view(request:HttpRequest):
    theme = request.COOKIES.get('theme', 'light')
    return render(request, 'Main/about.html', {'theme': theme})

def contact_us(request:HttpRequest):
    theme = request.COOKIES.get('theme', 'light')
    return render(request, 'Main/contact_us.html', {'theme': theme})