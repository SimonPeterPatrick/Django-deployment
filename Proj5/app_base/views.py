from django.shortcuts import render
from app_base.forms import UserProfilForm,UserProfilInfo

#Do logowania
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect


def user_login(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        
        if user:
            if user.is_active:
                
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            
            else:
                return HttpResponse("User is not active")
            
        else:
            return HttpResponse("Invalid login arguments")
    else:        
        return render(request,'app_base/login.html',{})
   
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))     

@login_required
def special(request):
    return HttpResponse("You are loggin in")


# Create your views here.

def index(request):
    return render(request,'app_base/index.html')

def register(request):
    
    registered1 = False
    
    if request.method == 'POST':
#        dobieranie sie do wysylanych danych z forms
        user_form = UserProfilForm(data=request.POST)
        profile_form = UserProfilInfo(data=request.POST)
        
        if user_form.is_valid() and profile_form.is_valid():
            
            user = user_form.save()
            user.set_password(user.password)
            user.save()
    
            profile = profile_form.save(commit=False)
            profile.user = user
    
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
                
            profile.save()
            registered1 = True
        
        else: 
            print(user_form.error, profile_form.error)
    else:
        user_form = UserProfilForm()
        profile_form = UserProfilInfo()
        
    return render(request,'app_base/register.html',{'user_form':user_form,
                                               'profile_form':profile_form,
                                               'registered':registered1})