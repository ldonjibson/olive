from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.sites.shortcuts import get_current_site
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.validators import RegexValidator
from django.db.models import Q
from django.template.loader import render_to_string
from django.db import IntegrityError, transaction
import random
from .tokens import account_activation_token
from django.utils.encoding import force_bytes, force_text, smart_text 
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils import timezone
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect 
from django.contrib.auth.models import User
from .forms import ProfileUpdateForm, UserProfile, SignUpForm, UserUpdateForm
from coreconfig import tasks

def signup(request):
  context=''
  if request.method == 'POST':
    form = SignUpForm(request.POST)
    if form.is_valid():
      user = form.save(commit=False)
      user.is_active = True
      user.save()
      current_site = get_current_site(request)
      uid = urlsafe_base64_encode(force_bytes(user.pk))
      print(uid)
      # if len(config) == 0:
      subject = 'Activate SiteName'
      message = render_to_string('users/account_activation_email.html',{
        'username': user.username,'domain': current_site.domain,'uid': uid,'token': account_activation_token.make_token(user),
      })
      tasks.sending_mail(subject, message, user.email)
      # else:
      #   subject = 'Activate Your SiteName Account'
      #   message = render_to_string('users/account_activation_email.html',{
      #     'username': user.username,'domain': current_site.domain,'uid': uid,'token': account_activation_token.make_token(user),
      #   })
      #   tasks.sending_mail(subject, message, user.email)
      return redirect('users:account_activation_sent')
  else:
    form = SignUpForm()
    context	= {
    'register_form': form,
    }
    return render(request, 'users/register.html', context)
  return render(request, 'users/register.html', context)

def activate(request, uidb64, token):
    try:
    	uid = force_text(urlsafe_base64_decode(uidb64))
    	user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, UserModel.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):    	
        user.is_active = True
        user.save()
        user.user_profile.email_confirmed = True
        user.user_profile.save()
        current_site = get_current_site(request)
        config = []#DashboardConfig.objects.all()
        if len(config) == 0:
	        subject = 'Your Account is Activated'
	        message = render_to_string('users/account_activation_email_followup.html', {
	        	'username': user.username,
	        	'domain': current_site.domain,
	        	})
	        tasks.sending_mail(subject, message, user.email)
        else:
	        subject = 'Your Account is Activated'
	        message = render_to_string('users/account_activation_email_followup.html', {
	        	'username': user.username,
	        	'domain': current_site.domain,
	        	})
	        tasks.sending_mail(subject, message, user.email)
		##############################################
        user.backend = 'django.contrib.auth.backends.ModelBackend'
        login(request, user)
        return HttpResponseRedirect('/users/dashboard')
    else:
        return render(request, 'users/account_activation_invalid.html')

def get_absolute_url(self):
		return reverse('users:activate')

@login_required(login_url='/users/login')
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('users:change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'users/change_password.html', {
        'form': form
    })


def LoginView(request):
	return render(request, 'users/login.html', {})

def ProfilePage(request, username):
  # username = username.split('@')
  context=''
  user = request.user
  getUser = get_object_or_404(User, username=username.lower())
  getUserProfile = UserProfile.objects.get(user=getUser)
  profileForm = ProfileUpdateForm(instance=getUserProfile)
  userExtended = UserUpdateForm(instance=getUser)
  if request.method == 'POST':
    profileForm = ProfileUpdateForm(request.POST, request.FILES, instance=getUserProfile)
    userForm = UserUpdateForm(request.POST, instance=getUser)
    if profileForm.is_valid() and userForm.is_valid():
      userEx = userForm.save(commit=False)
      userProfile = profileForm.save(commit=False)
      print(userProfile.location)
      userEx = userEx.save()
      userProfile = profileForm.save()

      print('done')
  if user == getUserProfile.user:
    context = {
      "profileForm": profileForm,
      "userExtended": userExtended,
      "getUserProfile":getUserProfile,
      "user":user
    }
  else:
    context = {
      "profileForm": profileForm,
      "userExtended": userExtended,
      "getUserProfile":getUserProfile,
      "user":getUserProfile.user
    }
  return render(request, 'users/profile.html', context)

# def ProfileUpdateForm(request)

def DashBoardPage(request):
  return render(request, 'users/dashboard.html', {})

def DashBoardRedirect(request):
  return redirect('users:dashboard')

def MembersList(request):
  user = request.user
  members = User.objects.all().exclude(pk=user.id)
  return render(request, 'users/dashboard.html', {'members':members})