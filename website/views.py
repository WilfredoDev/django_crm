from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Record
from .forms import addRecordForm

def home(request):
    records = Record.objects.all()


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
        return render(request, 'home.html', {'records':records})

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

def single_record(request,pk):
    if(request.user.is_authenticated):
        single_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'single_record':single_record})
    else:
        messages.success(request, 'Debes haber iniciado sesion para acceder a esta pagina')
        return redirect('home')

def delete_record(request, pk):
    if (request.user.is_authenticated):
        record = Record.objects.get(id=pk)
        record.delete()
        messages.success(request, 'El registro ha sido borrado correctamente')
        return redirect('home')
    else:
        messages.success(request, 'Debes haber iniciado sesion para acceder a esta pagina')
        return redirect('home')
    
def add_record(request):
    form = addRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method=='POST':
            if form.is_valid():
                add_record = form.save()
                messages.success(request, "El registro ha sido creado correctamente")
                return redirect('home')
        return render(request, 'add.html', {"form":form})
    else:
        messages.success(request, "Hubo un error registrandote, intentalo de nuevo")
        return redirect('home')
    
def update_record(request, pk):
    if(request.user.is_authenticated):
        current_record = Record.objects.get(id=pk)
        form = addRecordForm(request.POST or None, instance=current_record)
        if(form.is_valid()):
            form.save()
            messages.success(request, "Registro actualizado correctamente")
            return redirect('home')
        return render(request, 'update.html', {'form':form})
    else:
        messages.success(request, "Hubo un error registrandote, intentalo de nuevo")
        return redirect('home')