from django.shortcuts import render

from django.utils import timezone

from .models import Post

def post_list(request):
	
	posts = Post.objects.filter(published_date_lte=timezone.now()).order_by('published')
	
	return render(request, 'frogblog/post_list.html', {'posts' : posts})
