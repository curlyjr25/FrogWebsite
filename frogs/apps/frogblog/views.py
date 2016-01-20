from django.shortcuts import render

def post_list(request):
	return render(request, 'frogblog/post_list.html', {})
