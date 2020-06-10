from django.shortcuts import render,redirect,get_object_or_404
import datetime as dt
from django.http import HttpResponse, Http404,HttpResponseRedirect
from django.db.models.base import ObjectDoesNotExist
from .models import Image, UserProfile
from .forms import ProfileForm,SignUpForm,PhotoForm
from .email import send_welcome_email
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.views.generic import TemplateView,RedirectView
from django.db import transaction
from django.urls import reverse
# Create your views here.

def welcome(request):
    
    return render(request, 'home.html')

def allphotos(request):
    photos=Image.objects.all()
    return render(request, 'allphotos.html', {"photos":photos})


def search_results(request):

    if 'photo' in request.GET and request.GET["photo"]:
        search_term = request.GET.get("photo")
        searched_photos =Image.search_by_name(search_term)
        message = f"{search_term}"

        return render(request, 'all-pics/search.html',{"message":message,"photos": searched_photos})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-pics/search.html',{"message":message})


def photo(request,photo_id):
    try:
        photo = Image.objects.get(id =photo_id)
    except ObjectDoesNotExist:
        raise Http404()
    return render(request,"all-pics/pic.html", {"photo":photo})
@login_required
def uploadphoto(request,user_id):
    if request.method=="post":
        form=PhotoForm(request.POST, request.FILES,)
        if form.is_valid():
            name = form.cleaned_data['name']
            caption = form.cleaned_data['caption']
            image= form.cleaned_data['image']
            photo=Image(name=name, caption=caption,image=image)
            photo.save_image()
            HttpResponseRedirect('allphotos.html')
    else:
        form = PhotoForm()
    return render(request, 'uploadphoto.html', {"form":form})




def today_posts(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            bio = form.cleaned_data['bio']
            profilephoto= form.cleaned_data['image']
            recipient = UserProfile(name = name,email =email, bio=bio,profilephoto=profilephoto)
            recipient.save()
            HttpResponseRedirect('today_posts.html')
    else:
        form = ProfileForm()
    return render(request, 'profile.html', {"profileForm":form})


def registerPage(request):
    
    if request.method=="POST":
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('login')
    else: 
        form=SignUpForm()
    
    return render(request, 'django_registration/registration_form.html', {'form':form})
def login_view(request):
    
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        
        if user is not None:

            login(request, user)

            return redirect('allphotos')
        else:
            return HttpResponse("invalid login credentials")
    
    return render(request, 'django_registration/login.html')

@login_required      
def logout_view(request):
    logout(request)
    return redirect('login')

  
@login_required
@transaction.atomic
def updateprofile(request, user_id):

    if not request.user.is_authenticated:
        return redirect('django_registration/login.html')
    else:
        if request.method == 'POST':
            user_form = SignUpForm(request.POST, instance=request.user)
            profile_form = ProfileForm(request.POST,request.FILES, instance=request.user)
            if user_form.is_valid() and profile_form.is_valid():
                user_form.save() 
                profile_form.save()
                messages.success(request, ('Your profile was successfully updated!'))
                return HttpResponseRedirect(reverse("allphotos" ))
            else:
                messages.error(request, ('Please correct the error below.'))
        else:
            user_form = SignUpForm(instance=request.user)
            profile_form = ProfileForm(instance=request.user)
        return render(request, 'update_profile.html', {'user_form': user_form,'profile_form': profile_form})
@login_required
def userprofile(request, user_id):
    if not request.user.is_authenticated:
        return redirect('django_registration/login.html')
    else:
        user=User.objects.get(id=user_id)       
        return render(request,'profile.html',{'user':user})


def increment_counter(request,photo_id):
    if not request.user.is_authenticated:
        return redirect('django_registration/login.html')
    else:
        if request.method=="POST":
            if 'like' in request.POST:
                liked = get_object_or_404(Image, id=request.POST.get('photo_id'))
                liked.likes.add(request.user)
                
            return HttpResponseRedirect(reverse("liked", args=[str(photo_id)]) )#check this too
# 
