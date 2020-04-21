from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import Comment
from .forms import CommentForm

def index(request):
	comments = Comment.objects.order_by('-date_added')

	context = {'comments' : comments}

	return render(request, 'guessbook/index.html', context)

def contact_us(request):
	if request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			new_comment = Comment(name = request.POST['name'] , comment=request.POST['comment'])
			new_comment.save()
			return HttpResponseRedirect('/guessbook')
	else:
		form =CommentForm()

	context ={'form' : form}
	return render(request,'guessbook/contact_us.html',context)

def single(request):
	return render(request, 'guessbook/single.html')

def blog(request):
	return render(request, 'guessbook/blog.html')


