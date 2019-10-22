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
		return redirect('/wall')

def clear(request):
	request.session.clear()
	return redirect('/')


def wall(request):
	this_user = Reg.objects.get(id=request.session['userid'])
	all_messages = Message.objects.all().order_by('-updated_at')
	# a_message = Message.objects.get(id=1)
	# comments = a_message.comments.all()
	comments = Comment.objects.all()

	context = {
		"user" : this_user,
		"messages" : all_messages,
		"comments" : comments
	}
	return render(request, 'app1/wall.html', context)

def postm(request):

	if request.method == "POST":
		Message.objects.create(message=request.POST['message'], reg=Reg.objects.get(id=request.session['userid']))
	return redirect('/wall')

def postc(request):
	if request.method == "POST":
		num = request.POST['mess']
		mess = Message.objects.get(id=num)
		Comment.objects.create(comment=request.POST['comment'],  reg=Reg.objects.get(id=request.session['userid']), message=mess)
	return redirect('/wall')

def delete(request):
	if request.method == "POST":

		number = request.POST['delete']

		Message.objects.get(id=number).delete()
	return redirect('/wall')		