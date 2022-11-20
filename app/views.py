from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login as loginuser,logout
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from app.forms import TODOForm
from app.models import TODO
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required(login_url='Login')
def home(request):
    if request.user.is_authenticated:
        user = request.user
        form = TODOForm()
        todos = TODO.objects.filter(user = user).order_by('priority')
        return render(request , 'index.html' , context={'form' : form , 'todos' : todos})
def Login(request):
  if request.method == 'GET':
        form1 = AuthenticationForm()
        context = {
            "form" : form1
        }
        return render(request , 'Login.html' , context=context )
  else:
        form = AuthenticationForm(data=request.POST)
        print(form.is_valid())
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username , password = password)
            if user is not None:
                loginuser(request , user)
                return redirect('home')
        else:
            context = {
                "form" : form
            }
            return render(request , 'Login.html' , context=context )


def Signup(request):
   if request.method== 'GET':
    form = UserCreationForm()
    context = {
        "form" : form
    }
    return render(request,'Signup.html',context=context)
   else:
      print(request.POST)
      form = UserCreationForm(request.POST)
      context = {
        "form" : form
    }
      if form.is_valid():
        user = form.save()
        print(user)
        if user is not None:
            return redirect('Login')
      else:
         return render(request,'Signup.html',context=context)


def add_todo(request):
    if request.user.is_authenticated:
        user = request.user
        print(user)
        form = TODOForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            todo = form.save(commit=False)
            todo.user = user
            todo.save()
            print(todo)
            return redirect("home")
        else: 
            return render(request , 'index.html' , context={'form' : form}) 


def delete_todo(request , id ):
    print(id)
    TODO.objects.get(pk = id).delete()
    return redirect('home')

def change_todo(request , id  , status):
    todo = TODO.objects.get(pk = id)
    todo.status = status
    todo.save()
    return redirect('home')


def signout(request):
    logout(request)
    return redirect('login')