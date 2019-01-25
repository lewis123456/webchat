from webchatlib.response import check_response


@check_response
def handle_user(request, *args, **kwargs):
	return {
		'hello': 'world',
	}
