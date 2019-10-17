from django.shortcuts import render, redirect
import bcrypt
from .models import *
from django.contrib import messages

def index(request):
	return render(request, 'app1/index.html')

def register(request):
	errors = Reg.objects.basic_validator(request.POST)
	if len(errors) > 0:
		for key, value in errors.items():
			messages.error(request, value)
		return redirect('/')
	else:
		if request.method == "POST":
			password = request.POST['password']
			pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

			user = Reg.objects.create(first=request.POST['first'], last=request.POST['last'], email=request.POST['email'], password=pw_hash)
			request.session['userid'] = user.id
			messages.success(request, "Successfully logged in")
			return redirect('/success')

def login(request):

	if request.method == "POST":
		email = Reg.objects.filter(email=request.POST['l_email'])
		if email:
			user = email[0]
			if bcrypt.checkpw(request.POST['l_password'].encode(), user.password.encode()):
				request.session['userid'] = user.id

				return redirect('/success')
			else: 
				messages.error(request, "Incorrect password")
				return redirect('/')
		else:
			messages.error(request, "User does not exist")
			return redirect('/')

def success(request):
	if 'userid' not in request.session:
		return redirect('/')
	else:
		num = request.session['userid']
		context = {
			"user" : Reg.objects.get(id=num)
		}
		return render (request, 'app1/success.html', context)

def clear(request):
	request.session.clear()
	return redirect('/')