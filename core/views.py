from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.forms import forms
from django.shortcuts import render, redirect


# Create your views here.
from core.forms import SignUpForm
from core.models import NewsFeeds, reminder


@login_required
def home(request):
    nwfeed = NewsFeeds.objects.all()
    remind = reminder.objects.all()
    return render(request, 'core/home.html', {'nwfeed':nwfeed, 'remind':remind})

def index(request):
    return render(request, 'core/index.html')

def base(request):
    return render(request, 'core/base.html')

# def signup(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             sem = form.cleaned_data.get('sem')
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#             return redirect('core:home')
#     else:
#         form = UserCreationForm()
#     return render(request, 'core/signup.html', {'form': form})
#
# def signup(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#             return redirect('core:home')
#     else:
#         form = SignUpForm()
#     return render(request, 'core/signup.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.dept = form.cleaned_data.get('dept')
            user.profile.sem = form.cleaned_data.get('sem')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('core:home')
    else:
        form = SignUpForm()
    return render(request, 'core/signup.html', {'form': form})


from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver

@receiver(user_logged_in)
def got_online(sender, user, request, **kwargs):
    user.profile.is_online = True
    user.profile.save()

@receiver(user_logged_out)
def got_offline(sender, user, request, **kwargs):
    user.profile.is_online = False
    user.profile.save()