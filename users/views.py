from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import userRegisterForm
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method=="POST":
        form = userRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'Account Created For {username}!')
            return redirect('login')
            
    else:
        form = userRegisterForm()
    return render(request,'users/form.html',{'form':form})

@login_required
def profile(requests):
    return render(requests,'users/profile.html')