import json
import functools
from django.http import HttpResponse


def json_response(json_object, status=200, location=None, per_page=None, total=None, encoder=None):
	try:
		content = json.dumps(json_object, cls=encoder)
	except:
		content = json.dumps(json_object, encoder='latin1', cl=encoder)
	response = HttpResponse(content, status=status, content_type='application/json')
	if location:
		response['Location'] = location
	if per_page:
		response['Per-Page'] = per_page
	if total:
		response['Total'] = total
	return response


def check_response(fn):
	@functools.wraps(fn)
	def inner(*args, **kwargs):
		ret = fn(args, kwargs)
		if not isinstance(ret, HttpResponse):
			if isinstance(ret, (dict, list)):
				return json_response(ret)
		return ret
	return inner

