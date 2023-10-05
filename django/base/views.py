from django.shortcuts import render, redirect
from base.forms import ContatoForm, ReservaForm

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout



def inicio(request):
    return render(request, "index.html")




def contato(request):
    sucesso = False

    if request.method == 'GET':
        form = ContatoForm()
    else:
        form = ContatoForm(request.POST) 

        if form.is_valid():
            sucesso = True
            form.save()

    contexto = {
        'telefone': '(42) 99937-1559',
        'responsavel': 'Geovane Joanico',
        'formulario': form,
        'sucesso': sucesso
    }


    return render(request, "contato.html", contexto)





def reserva(request):
    if request.method == 'GET':
        form = ReservaForm()
    else:
        form = ReservaForm(request.POST)
        if form.is_valid():
            form.save()


    contexto = {    
        'form': form    
    }


    return render(request, "reserva.html", contexto)        



def login_usuario(request):
    if request.method == 'GET':
        formulario = AuthenticationForm()
        contexto = {
            'formulario': formulario
        }
        return render(request, "login.html", contexto)
    
    else:
        nome_usuario = request.POST['username']
        senha = request.POST['password']
        usuario = authenticate(request, username=nome_usuario, password=senha)
        if usuario is not None:
            login(request, usuario)
            return redirect("inicio")
        
#view de logout de usuário
def logout_usuario(request):
    logout(request)
    return redirect("inicio")    

#view de criação de usuario
def cadastro_usuario(request):
    if request.method == 'GET':
        formulario = UserCreationForm()

    else:
        formulario = UserCreationForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect("inicio")
        
    contexto = {
        "formulario": formulario
    }

    return render(request, "cadastro_usuario.html", contexto)