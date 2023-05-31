from django.urls import path, include
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'webapp'


urlpatterns = [
path('', views.index, name= 'index'),
path('about_me/',login_required(login_url='/login/')(views.about_me), name='about_me'),
path('contact/',views.contact, name='contact'),
path('dashboard/',login_required(login_url='/login/')(views.dashboard),name='dashboard')
]