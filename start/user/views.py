#coding:utf-8

from django.shortcuts import render
from django.http import HttpResponse

from django.http import HttpResponseRedirect,Http404
from django.contrib.auth import logout # 匯入logout函式
from django.urls import reverse

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User,Permission

from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
        return render(request,'user/index.html')

def logout_view(request): # 呼叫logout函式，它會把request當作引數，然後重新導向主頁
    logout(request)
    return HttpResponseRedirect(reverse('user:index'))

def register(request):
    """Register a new user."""
    if request.method != 'POST':  
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)
        
        if form.is_valid():
            new_user = form.save()
			
            user = User.objects.get(username=new_user.username)
            user.is_staff = True
            user.save()
            user.user_permissions.add(Permission.objects.get(codename='can_view'))
            user.user_permissions.add(Permission.objects.get(codename='can_add'))
            user.user_permissions.add(Permission.objects.get(codename='can_see'))
            user.user_permissions.add(Permission.objects.get(codename='can_edit'))
            user.user_permissions.add(Permission.objects.get(codename='can_delete'))
            user.save()
            #new_user.user_permissions = [Permission.objects.get(codename='can_view'),Permission.objects.get(codename='can_add')]   #给予 浏览、添加 权限
            authenticated_user = authenticate(username=new_user.username,
                password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('user:index'))

    context = {'form': form}
    return render(request, 'user/register.html', context)

