from django.conf.urls import patterns, include, url
from api.views import urls

urlpatterns = patterns(
	'',
	url(r'^api/v1', include(urls)),
)
