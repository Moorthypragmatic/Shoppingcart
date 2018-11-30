from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect

# Create your views here.

def index(request):
    return render(request,'user_example/index.html')
def shop(request):
    return render(request,'user_example/shop.html')

def register(request):
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)        
            return redirect('index')       

    else:
        form = UserCreationForm()
    context = {'form': form}
    return render(request,'registration/register.html',context)

def cartdetails(request):
    return render(request,'user_example/addcart.html')

def productdetails(request):
    return render(request,'user_example/product_details.html')

def checkout(request):
    return render(request,'user_example/checkoutpage.html')
