from django.shortcuts import render
from .models import Post
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/login/')
def blog_home(request):
    posts = Post.objects.all()
    return render(request, 'blog.html', {'posts': posts})

