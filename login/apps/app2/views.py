from django.shortcuts import render
from .models import *
# Create your views here.
def wall(request):
	this_user = User.objects.get(id=request.session['userid'])
	all_messages = Message.objects.all().order_by('updated_at')
	# a_message = Message.objects.get(id=1)
	# comments = a_message.comments.all()
	comments = Comment.objects.all()
	context = {
		"user" : this_user,
		"messages" : all_messages,
		"comments" : comments
	}
	return render(request, 'app2/wall.html', context)

def postm(request):
	if request.method == "POST":
		Message.objects.create(message=request.post['message'], user="Bob")
	return redirect('/wall')