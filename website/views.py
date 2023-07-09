from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User

def home(request):
    #check to see if logging in
    if (request.method =='POST'):
        username = request.POST['username']
        password = request.POST['password']

        #authenticate credentials
        user = authenticate(request, username=username, password=password)
        if  (user!=None):
            login(request,user)
            messages.success(request, "Te has logueado correctamente")
            return redirect('home')
        else:
            messages.success(request, "There was an error loggin in, please try agaim")
            return redirect('home')
    else:
        return render(request, 'home.html', {})

def login_user(request):
    pass

def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        
        # Crea un nuevo usuario utilizando los datos del formulario
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        current_user = authenticate(username=username, password=password)
        if  (current_user!=None):
            login(request,user)
            messages.success(request, "Te has Registado correctamente")
            return redirect('home')
        else:
            messages.success(request, "Hubo un error registrandote, intentalo de nuevo")
            return redirect('home')
        # Realiza cualquier otra acción necesaria después de crear el usuario
        
        return redirect('home')  # Redirige a la página de inicio después del registro
    
    return render(request, 'register.html')
