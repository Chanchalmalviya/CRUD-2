from django.shortcuts import render,redirect
from django.http import HttpResponse
from.models import*
from django.contrib.auth.hashers import make_password


# Create your views here.

#def index(request):
   # return HttpResponse("this is my firstproject")

def index(request):
    return render(request,"index.html")

def add_users(request):
    if request.method == "POST":
     email = request.POST['email']
     phone = request.POST['phone']
     password = make_password(request.POST['password'])

    if Person.objects.filter(email=email).exists():
       return HttpResponse("Email is allready exists")
    elif Person.objects.filter(phone=phone).exists():
       return HttpResponse("Phone number is allready exists")
    else:
       Person.objects.create(email=email,phone=phone,password=password)
       return HttpResponse("User crrated")
     
def data(request):
    user = Person.objects.all()
    return render(request,"table.html",{"user":user})

def user_delete(request,pk):
   Person.objects.get(id=pk).delete()
   return redirect("/table/")

def update_user(request,uid):
   user_obj = Person.objects.get(id=uid)
   return render(request,"update.html",{"user_obj":user_obj})

def update_views(request):
   if request.method == 'POST':
      uid = request.POST['uid']
      email = request.POST['email']
      phone = request.POST['phone']
      Person.objects.filter(id=uid).update(email=email,phone=phone)
      return redirect('/table/')