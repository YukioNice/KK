from django.shortcuts import render
def index(request):
    return render(request, "home.html")
def indexA(request):
    return render(request, "about.html")