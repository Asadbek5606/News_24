from .models import Destination
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import Image
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth import authenticate

# Create your views here.

def Index(request):
    pics = Image.objects.all()
#     dest1 = Destination()
#     dest1.name = 'Trending'

    dests = Destination.objects.all()
    return render(request, IndexView, {'pics': pics})




# class la bilan TemplateView bilan ishlash

class IndexView(TemplateView):
    
    template_name = "index.html"


class BlogView(TemplateView):
    template_name = "blog.html"



class SingleView(TemplateView):
    template_name = "single.html"


class ContactView(TemplateView):
    template_name = "Contact_us.html"



def registration(request):
    form = CreateUserForm()
    
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('login')
    
    context = {'form': form}
    return render(request, 'registration.html', context)


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = auth.authenticate(request, username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Username OR Password is incorrect')
            
    return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('login')
