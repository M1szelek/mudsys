from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mudsys.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^(/)?$', RedirectView.as_view(url='/accounts/login')),
     #url(r'^(/)?$', include('django.contrib.auth.urls'))
     url(r'^chats/', include('chat.urls', namespace='chat')),
     url(r'^pm/', include('privmsg.urls', namespace='privmsg')),
     url(r'^files/', include('fileman.urls', namespace='fileman')),
     url(r'^history/', include('history.urls', namespace='history')),
     url(r'^tasks/', include('taskman.urls', namespace='taskman')),
     url(r'^admin/', include(admin.site.urls)),
     url(r'^accounts/login/$',  'mudsys.views.login'),
    url(r'^accounts/auth/$',  'mudsys.views.auth_view'),    
    url(r'^accounts/logout/$', 'mudsys.views.logout'),
    url(r'^accounts/loggedin/$', 'mudsys.views.loggedin'),
    url(r'^accounts/invalid/$', 'mudsys.views.invalid_login'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
