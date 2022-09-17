from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages

from .models import Profile
# Create your views here.


def index(request):
    return render(request, 'index.html',)


def signUp(request):
    
    if request.method == "POST":
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']

        if User.objects.filter(email=email).exists():
            messages.info(request, "email has been taken")
            return redirect('signup')
        else:
            user = User.objects.create(
                first_name=first_name, last_name=last_name, username=username, email=email)
            user.save()
            
            # user_model = User.objects.get(email=email)
            # new_profile = Profile.objects.create(user = user_model)
            # new_profile.save()
            return redirect('signup')
    else:
        return render(request, 'register.html',)


def usersList(request):
    users = User.objects.all()
    context= {"users" : users }
    return render(request, 'users_list.html', context)