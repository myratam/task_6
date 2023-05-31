from django.views.generic import ListView, DetailView
from django.urls import path
from .models import Post
from blog.views import blog_home
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('',
        login_required(login_url='/login/')(
            ListView.as_view(
                queryset=Post.objects.all().order_by("-date")[:25],
                template_name="blog.html"
            )
        ),
        name='blog_home'
    ),
    path('<int:pk>/',
        login_required(login_url='/login/')(
            DetailView.as_view(
                model=Post,
                template_name="post.html"
            )
        ),
        name='blog_detail'
    ),
    path('blog/', blog_home, name='blog_home'),
    path('', ListView.as_view(), name='blog_home'),
    path('<int:pk>/', DetailView.as_view(), name='blog_detail'),
]