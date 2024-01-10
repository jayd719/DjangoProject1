from django.shortcuts import render
from .models import Post
from django.contrib.auth.decorators import login_required

@login_required
def home(requests):
    context = {'posts':Post.objects.all()}
    return render(requests,'blog/home.html',context)

@login_required
def about(requests):
    context = {'tilte':"ABOUT PAGE JI",'value':"THIS IS ABOUT PAGE"}
    return render(requests,'blog/about.html',context)

# Create your views here.
