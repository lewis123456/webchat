from django.conf.urls import patterns, include, url
from api.views import session, user, message, conversation

urlpatterns = patterns(
	'',
	url(r'^/session$', session.views.handle_session),
	url(r'^/sessions', include('api.views.session.urls')),
	url(r'^/user$', user.views.handle_user),
	url(r'^/users', include('api.views.user.urls')),
	url(r'^/message$', message.views.handle_message),
	url(r'^/messages', include('api.views.message.urls')),
	url(r'^/conversation$', conversation.views.handle_conversation),
	url(r'^/conversations', include('api.views.conversation.urls')),
)
