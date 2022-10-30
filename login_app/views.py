from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,PasswordChangeForm
from django.contrib.auth import login,authenticate,logout
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm,UserProfileChangeForm,ProfilePicChangeForm
# Create your views here.
def sign_up(request):
    form = SignUpForm()
    registered = False
    if request.method == 'POST':
        form = SignUpForm(data=request.POST)
        if form.is_valid():
            form.save()
            registered = True
    dict = {'form':form,'registered':registered}
    return render(request,'login_app\signup.html',context=dict)

def login_page(request):
    form = AuthenticationForm()
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect(reverse('home'))
    return render(request,'login_app\login.html',context={'form':form})

@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

@login_required
def user_profile(request):
    return render(request, 'login_app/userprofile.html',context={})

@login_required
def user_profile_change(request):
    current_user = request.user
    form = UserProfileChangeForm(instance=current_user)
    if request.method == 'POST':
        form = UserProfileChangeForm(request.POST,instance=current_user)
        if form.is_valid():
            form.save()
            form = UserProfileChangeForm(instance=current_user)
    return render(request,'login_app/userprofilechange.html',context={'form':form})

@login_required
def pass_change(request):
    changed=False
    current_user = request.user
    form = PasswordChangeForm(current_user)
    if request.method=='POST':
        form = PasswordChangeForm(current_user,data=request.POST)
        if form.is_valid():
            form.save()
            changed=True
            #return HttpResponseRedirect(reverse('login_app:profile'))
    return render(request,'login_app/passwordchange.html',context={'form':form,'changed':changed})

@login_required
def profile_pic_change(request):
    #changed=False
    #current_user = request.user
    form = ProfilePicChangeForm()
    if request.method=='POST':
        form = ProfilePicChangeForm(request.POST,request.FILES)
        if form.is_valid():
            user_obj = form.save(commit=False)
            user_obj.user = request.user
            user_obj.save()
            #changed=True
            return HttpResponseRedirect(reverse('login_app:profile'))
    return render(request,'login_app/profilepicchange.html',context={'form':form})
