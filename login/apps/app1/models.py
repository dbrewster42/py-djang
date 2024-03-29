from __future__ import unicode_literals
from django.db import models
import re
from datetime import datetime



class RegManager(models.Manager):
	def basic_validator(self, data):
		errors = {}
		if len(data['first']) < 2:
			errors['first'] = "Get yourself a longer name"
		if len(data['last']) < 2:
			errors['last'] = "Your name is not long enough"
		EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
		if not EMAIL_REGEX.match(data['email']):
			errors['email'] = "Invalid email address!"
		if Reg.objects.filter(email=data['email']):
			errors['email'] = "That email is already in use"
		if len(data['password']) < 8:
			errors['password'] = "Passwords must be at least 8 characters long"
		if data['confirm'] != data['password']:
			errors['confirm'] = "Your passwords do not match"
		return errors


class Reg(models.Model):
	first = models.CharField(max_length=30)
	last = models.CharField(max_length=30)
	email = models.CharField(max_length=40)
	password = models.CharField(max_length=40)
	objects = RegManager()

# class MessageManager(models.Manager):
# 	def validator(self, data):
# 		errors = {}
# 		Seconds = timedelta(data['create_at'])

# 		if datetime.strptime(data['created_at']) != datetime.today() &&  
# 		# datetime.strptime(data['date'], '%Y-%m-%d') > datetime.today(): datetime.datetime.now()
# 			errors['date'] = "You may only delete your post within 30 minutes"
# 		return errors

class Message(models.Model):
	message = models.TextField()
	reg = models.ForeignKey(Reg, related_name="messages")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	# objects = MessageManager()

class Comment(models.Model):
	comment = models.TextField()
	reg = models.ForeignKey(Reg, related_name="comments")
	message = models.ForeignKey(Message, related_name="comments")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)


