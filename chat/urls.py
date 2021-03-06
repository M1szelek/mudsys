from django.conf.urls import patterns, url
 
from chat import views
 
urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^bygroup/$', views.indexByGroup, name='indexByGroup'),
    url(r'^(?P<chat_room_id>\d+)/$', views.chat_room, name='chat_room'),
    url(r'^(?P<chat_room_id>\d+)/reply/$', views.reply, name='reply'),
)