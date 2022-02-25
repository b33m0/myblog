from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .forms import LoginForm, RegisterForm, ProfileForm
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.
def user_login(request):
    if request.method == 'GET':
        login_form = LoginForm() 
        return render(request=request, template_name='userprofile/login.html', context={ 'form': login_form })
    elif request.method == 'POST':
        login_form = LoginForm(data=request.POST)
        if login_form.is_valid():
            usrname=login_form.cleaned_data['username'] 
            pswd=login_form.cleaned_data['password']
            if authenticate(request, username=usrname, password=pswd) is not None:
                login(request, authenticate(request, username=usrname, password=pswd))
                return redirect("article:a_index")
            else:
                return HttpResponse("Invalid username or password")
        else:
            return HttpResponse("Please input the username and password")
    else:
        return HttpResponse("Invalid request")

def user_logout(request):
    logout(request)
    return redirect("article:a_index")

def user_register(request):
    if request.method == 'GET':
        register_form = RegisterForm()
        return render(request=request, template_name='userprofile/register.html', context={ 'form': register_form })
    elif request.method == 'POST':
        register_form = RegisterForm(data=request.POST)
        if register_form.is_valid():
            new_user = register_form.save(commit=False)
            pswd = register_form.cleaned_data['password2']
            new_user.set_password(pswd)
            new_user.save()
            login(request, new_user)
            return redirect("article:a_index")
        else:
            return HttpResponse("Invalid username or password")
    else:
        return HttpResponse("Invalid request")
        
@login_required(login_url='/userprofile/login/')
def profile_edit(request, id):
    user = User.objects.get(id=id)
    if Profile.objects.filter(user_id=id).exists():
        profile = Profile.objects.get(user_id=id)
    else:
        profile = Profile.objects.create(user=user)

    if request.method == 'GET':
        print('get success')
        profile_form = ProfileForm()
        context = { 'profile': profile, 'user': user }
        return render(request, 'userprofile/edit.html', context)
    elif request.method == 'POST':
        print('post success')
        if request.user != user:
            return HttpResponse('Illegal operation!')
        profile_form = ProfileForm(request.POST, request.FILES)
        if profile_form.is_valid():
            profile.profile_info = profile_form.cleaned_data['profile_info']
            if 'profile_img' in request.FILES:
                profile.profile_img = profile_form.cleaned_data['profile_img']
            profile.save()
            return redirect("userprofile:edit", id=id)
        else:
            return HttpResponse("Illeagal input!")
    else:
        return HttpResponse("Invalid request!")