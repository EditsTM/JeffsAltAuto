from django.shortcuts import render

def home(request):
    return render(request, 'main/home.html', {'page_name': 'home'})

def services(request):
    return render(request, 'main/services.html', {'page_name': 'services'})

def about(request):
    return render(request, 'main/about.html', {'page_name': 'about'})

def contact(request):
    return render(request, 'main/contact.html', {'page_name': 'contact'})