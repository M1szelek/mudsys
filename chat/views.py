from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
 
from chat.models import ChatRoom, Message

from django.contrib.auth.models import User, Group

from history.models import Change

import datetime
 
def index(request):
	chat_rooms = ChatRoom.objects.order_by('name')

	context = {
		'chat_list': chat_rooms,
	}
	return render(request,'chats/index.html', context)

def indexByGroup(request):
	chat_rooms = ChatRoom.objects.order_by('group__name')
	
	context = {
		'chat_list': chat_rooms,
	}
	return render(request,'chats/index.html', context)
 
def chat_room(request, chat_room_id):
	chat = get_object_or_404(ChatRoom, pk=chat_room_id)
	return render(request, 'chats/chat_room.html', {'chat': chat})

def reply(request, chat_room_id):
	chat = get_object_or_404(ChatRoom, pk=chat_room_id)
	#selected_choice = chat.message_set.get(pk=request.POST['choice'])
	m = Message()
	m.content = request.POST['message']
	m.datetime = datetime.datetime.now()
	m.user = request.user
	chat.message_set.add(m)

	descstr = "Nowy post w " + chat.name

	change = Change()
	change.datetime = datetime.datetime.now()
	change.description = descstr
	change.user = request.user
	change.save()
	#chat.save()
	return render(request, 'chats/chat_room.html', {'chat': chat})


