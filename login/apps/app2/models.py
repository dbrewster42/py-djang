from django.db import models

# class User(models.Model):
# 	name = models.CharField(max_length=255)
# 	password = models.CharField(max_length=255)
# 	created_at = models.DateTimeField(auto_now_add=True)
# 	updated_at = models.DateTimeField(auto_now=True)

# class Message(models.Model):
# 	message = models.TextField()
# 	user = models.ForeignKey(User, related_name="messages")
# 	created_at = models.DateTimeField(auto_now_add=True)
# 	updated_at = models.DateTimeField(auto_now=True)

# class Comment(models.Model):
# 	comment = models.TextField()
# 	user = models.ForeignKey(User, related_name="comments")
# 	message = models.ForeignKey(Message, related_name="comments")
# 	created_at = models.DateTimeField(auto_now_add=True)
# 	updated_at = models.DateTimeField(auto_now=True)