from django.shortcuts import render

# Create your views here.
from django.shortcuts import render ,redirect
from django.contrib.auth import logout ,login
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.http import HttpResponse,HttpRequest
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
from .forms import UserRegistrationForm

# Create your views here.

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    redirect_authenticated_user = True  # Redirige si déjà connecté
    success_url = reverse_lazy('menu') 

@login_required
def profile(request:HttpRequest)->HttpResponse:
    template_name='registration/profile.html'
    context= {
        'session':profile ,
    }
        
    return render(request,template_name , context)

def logout_view(request):
    logout(request)
    return redirect('acceuil')

def register_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        firstname = request.POST.get('firstname')
        password = request.POST.get('password')
        password2 =  request.POST.get ('password2')
        email = request.POST.get ('email')
        if password != password2:
            messages.error(request, "Les mots de passe ne correspondent pas.")
            return redirect("register")
        if User.objects.filter(username=username).exists():
            messages.error(request, "Le nom d'utilisateur est déjà pris.")
            return redirect("register")
        if User.objects.filter(email=email).exists():
            messages.error(request, "L'email est déjà utilisé.")
            return redirect("register")
        if password ==password2:
            new_user = User(
                username = username,
                firstname = firstname,
                email = email,
            )
            new_user.set_password(password)
            
            new_user.save()
            messages.success(request, f"Bienvenue {username}, votre compte a été créé avec succès !")
            login(request,new_user)
            return redirect("menu")
    else:
        form = UserRegistrationForm()

    return render(request, "registration/signup.html", {"form": form})


