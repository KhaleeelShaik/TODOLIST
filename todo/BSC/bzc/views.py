from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from . models import todo



@login_required(login_url='signin')
def fun (request):
    if request.method=='POST':
        task=request.POST.get('task')
        due=request.POST.get('due')
        todo.objects.create(task=task,due=due,uid_id=request.user.id)
    return render(request,"todo.html")

def signup(request):
    if request.method=="POST":
        username=request.POST.get('username')
        email=request.POST.get('email')
        task=request.POST.get('task')
        due=request.POST.get('due')
        password=request.POST.get('password')
        confirmpassword=request.POST.get("confirmpassword")
        if password == confirmpassword:
            user=User.objects.create_user(username=username,password=password,email=email)
            todo.objects.create(task=task,due=due,uid_id=user.id)
            return redirect('signin')
    return render (request,"signup.html")

def signin(request):
    if request .method == "POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(username=username,password=password,)
        if user is not None:
            login(request,user)
            return redirect("fun")
    return render(request,"signin.html")

def display(request):
    d=todo.objects.all()
    return render (request,"display.html",{"table":d})

def delete(request,id):
        todo.objects.filter(id=id).delete()
        return redirect("display")

def edit(request,id):
    if request.method=="POST":
        task=request.POST.get("task")
        status=request.POST.get("status")
        due=request.POST.get("due")
        todo.objects.filter(id=id).update(task=task,status=status,due=due)
        return redirect("fun")
    return render(request,"edit.html")

def search(request):
    if request.method=="POST":
        search=request.POST.get('search')
        task = todo.objects.filter(uid_id=request.user.id,task=search)
        print(task)
        return render(request,"index.html",{"table":task})
    return render (request,'display.html')

 
def finish (request,id):
    get_todo=todo.objects.get(id=id)
    get_todo.status = 1
    get_todo.save()
    return redirect("display")






        

