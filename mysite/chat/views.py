from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse


from .models import ChatRoom, User, Message

# Create your views here.

def index(request):

	chat_rooms = ChatRoom.objects.all()

	context = {'chat_rooms': chat_rooms }

	return render(request, 'chat/index.html', context)

def room(request, chatroom_id):

	#users = ChatRoom.objects.get(pk=chatroom_id).user_set.all()
	users = get_object_or_404(ChatRoom, pk=chatroom_id).user_set.all()


	return render(request, 'chat/room.html',
		{'users': users})
