from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth
from django.contrib import messages
from . models import User, Images
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from . forms import ImageForms





def home(request):
    images = Images.objects.all()
    context = {
        'images': images
    }
    return render(request, 'home.html', context)

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_superuser:
            auth.login(request, user)
            messages.success(request, "You have been successfully logged in")
            return redirect('home')
        else:
            if user is not None: 
                messages.error(request, "Invalid credentials")
                return redirect('login')
            else: 
                messages.error(request, "Access denied. This website is for viewing purpose only.")
    return render(request, 'gallery/login.html')    

def logout(request):
    auth.logout(request)
    messages.info(request, "you are now logout")
    return redirect('home')

def add_photo(request):
    if request.method == 'POST':
        form = ImageForms(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = request.user
            image.save()
            messages.success(request, "your image has been successfully")
            return redirect('home')
        else:
            print(form.errors)
    else:
        form=ImageForms()
    context = {
        'form' : form
    }
    return render(request, 'gallery/add_photo.html', context)  
         
         

def edit(request, pk):
    image = get_object_or_404(Images, pk=pk)
    if request.method == 'POST':
        form = ImageForms(request.POST, instance=image)
        if form.is_valid():
            form.save()
            messages.success(request, "Your changes have been updated successfully")
            return redirect('home')
    else:
        form = ImageForms(instance=image)
    context = {
        'form':form,
        'image': image
        }
    return render(request, "gallery/edit.html", context)
    
def delete(request, pk):
    image = get_object_or_404(Images, pk=pk)
    image.delete()
    messages.success(request, "Image Deleted")
    return redirect('home')


