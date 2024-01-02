from django.shortcuts import render


def home(requests):
    context = {'title':"HOME PAGE!",'value':"THIS IS HOME PAGE!pp"}
    return render(requests,'blog/home.html',context)

def about(requests):
    context = {'tilte':"ABOUT PAGE JI",'value':"THIS IS ABOUT PAGE"}
    return render(requests,'blog/about.html',context)

# Create your views here.
