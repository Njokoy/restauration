from django.shortcuts import render



def index(request):
    context = {"message": "Bienvenue sur mon site"}
    return render(request, "index.html", context)