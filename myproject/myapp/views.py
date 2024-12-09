from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth 
from django.contrib import messages
from django.http import HttpResponse
from .models import Feature

def index(request):
   ''''
   feature1= Feature()
   feature1.id=0
   feature1.name = "Slow"
   feature1.details="Our service is very quick"
   '''
   features = Feature.objects.all()
   return render(request,'index.html', {'features':features})


def register(request):
   if request.method == 'POST':
      username = request.POST['username']
      email= request.POST['email']
      Password = request.POST['Password']
      Repeat_Password= request.POST['Repeat Password']

      if Password == Repeat_Password:
         if User.objects.filter(email=email).exists():
            messages.info(request, 'Email already used')
            return redirect('register')
         elif User.objects.filter(username=username).exists():
            messages.info(request, 'Username already used')
            return redirect('register')
         else:
            user=User.objects.create_user(username=username, email=email, password=Password)
            user.save()
            return redirect('login')
      else:
         messages.info(request, "Password Not the same ")
         return redirect('register')
      
   else:
      return render(request, 'register.html')

def login(request):
   if request.method =="POST":
      username=request.POST['username']
      password=request.POST['Password']
      user= auth.authenticate(username=username, password=password)
      if user is not None:
         auth.login(request, user)
         return redirect('/')
      else:
         messages.info(request, 'Credentials Invalid')
         return redirect('login')
      
   else:
      return render(request, 'login.html')

def counter(request):
   posts=[1,2,3,4,5,'tim','tom','john']
   return render(request, 'counter.html', {'posts':posts})

def post(request, pk):
   return render(request, 'post.html', {'pk':pk})