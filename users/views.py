from django.shortcuts import render
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
from core.models import *
# Create your views here.



def register(request):
    if request.method == 'POST':
        user_form=RegisterForm(request.POST)
        if user_form.is_valid():
            if user_form.cleaned_data['password'] == user_form.cleaned_data['password2']:
                new_user=user_form.save(commit=False)
                new_user.set_password(user_form.cleaned_data['password'])
                new_user.save()
                Profile.objects.create(user=new_user)
                return render(request,'register_done.html')
    else:
        user_form=RegisterForm()
    return render(request, 'register.html', {'user_form':user_form})

@login_required
def edit(request):
    if request.method == 'POST':
        user_form=UserEditForm(instance=request.user, data=request.POST)
        profile_form=ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
    else:
        user_form=UserEditForm(instance=request.user)
        profile_form=ProfileEditForm(instance=request.user.profile)
    return render(request, 'edit.html', {'user_form':user_form, 'profile_form':profile_form} )

