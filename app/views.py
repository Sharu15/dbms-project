from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from django.utils import timezone
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
# from app.models import 


def signup(request):
	if request.method=="POST":
		username = request.POST.get('username',None)
		password = request.POST.get('password',None)
		email=request.POST.get("email")
		try:
			user = User.objects.get(username=username)
			print(user)
		except:
			user=None
		
		if user is not None:
			return render(request,'signup.html',{'show':'username.already.taken'})

		else:
			user=User.objects.create_user(username=username,email=email,password=password)	
			user.save()
			return redirect("/home/")
	return render(request, "signup.html")

def signin(request):
	if request.method=="POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect("/home/")
	return render(request,"signin.html")    	

def signout(request):
	logout(request)
	return redirect("/login/")	


def home(request):
	return render(request,"home.html")

def about(request):
	return render(request,"about.html")	