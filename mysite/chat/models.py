from django.db import models

# Create your models here.

class ChatRoom(models.Model):

	room_name = models.CharField(max_length=50)

	room_create_time = models.DateTimeField('creation time')

	def __str__(self):
		return self.room_name

class User(models.Model):


	chat_room = models.ForeignKey(ChatRoom,
		on_delete=models.CASCADE)

	username = models.CharField(max_length=20)

	def __str__(self):
		return self.username

class Message(models.Model):

	user = models.ForeignKey(User,
		on_delete=models.CASCADE)

	message_text = models.CharField(max_length=200)

	message_time = models.DateTimeField('message time')

	def __str__(self):
		return self.message_text 




