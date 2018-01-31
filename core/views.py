# Create your views here.
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect,get_object_or_404,HttpResponse
from core.forms import SignUpForm,UserForm,ProfileForm
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Profile,Team,Events
from django.urls import reverse
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user=form.save()
            user.refresh_from_db()
            user.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('core:update_profile')
    else:
        form = SignUpForm()
    return render(request, 'core/signup.html', {'form': form})

@login_required
def myprofile(request):
    
    return render(request, 'core/my_profile.html')   

@login_required
@transaction.atomic
def update_profile(request):

    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, ('Your profile was successfully updated!'))
            return redirect('core:profile')
        else:
            messages.error(request, ('Please correct the error below.'))        
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
        
        
    return render(request,'core/update_profile.html',{
        'user_form': user_form,
        'profile_form': profile_form,
        })   
        

def events_detail(request):
    events=Events.objects.all()
    context={'events':events,}
    return render(request,'core/events_detail.html',context)

def detail_of_event(request,id):
    instance=get_object_or_404(Events,id=id)
    context={'event':instance,}
    return render(request,'core/detail_of_event.html',context)

@login_required
def register_in_event(request,id):
    instance=get_object_or_404(Events,id=id)
    request.user.profile.events.add(instance)
    request.user.profile.events.amount=0
    amount=0
    queryset=request.user.profile.events.all()
    for event in queryset:
        amount=amount+event.fee
        print(amount)
    request.user.profile.amount=amount
    print(request.user.profile.amount)
    request.user.profile.save()    
    return redirect(instance)


