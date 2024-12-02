from django.shortcuts import render, redirect
from admin_material.forms import LoginForm, RegistrationForm, UserPasswordResetForm, UserSetPasswordForm, UserPasswordChangeForm
from django.contrib.auth import logout
from django.contrib.auth import views as auth_views

# Create your views here.


def index(request):
    context = {
        'segment': 'dashboard'
    }
    return render(request, 'pages/index.html', context)

def tables(request):
    context = {
        'segment': 'tables'
    }
    return render(request, 'pages/tables.html', context)


def billing(request):
    context = {
        'segment': 'billing'
    }
    return render(request, 'pages/billing.html', context)

def virtual_reality(request):
    context = {
        'segment': 'virtual_reality'
    }
    return render(request, 'pages/virtual-reality.html', context)

def rtl(request):
    context = {
        'segment': 'rtl'
    }
    return render(request, 'pages/rtl.html', context)

def notifications(request):
    context = {
        'segment': 'notifications'
    }
    return render(request, 'pages/notifications.html', context)

def profile(request):
    context = {
        'segment': 'profile'
    }
    return render(request, 'pages/profile.html', context)


def map(request):
    context = {
        'segment': 'map'
    }
    return render(request, 'pages/map.html', context)

def typography(request):
    context = {
        'segment': 'typography'
    }
    return render(request, 'pages/typography.html', context)

def icons(request):
    context = {
        'segment': 'icons'
    }
    return render(request, 'pages/icons.html', context)

def template(request):
    context = {
        'segment': 'template'
    }
    return render(request, 'pages/template.html', context)


class UserLoginView(auth_views.LoginView):
  template_name = 'pages/sign-in.html'
  form_class = LoginForm
  success_url = '/'

def register(request):
  if request.method == 'POST':
    form = RegistrationForm(request.POST)
    if form.is_valid():
      form.save()
      print('Account created successfully!')
      return redirect('/accounts/login/')
    else:
      print("Registration failed!")
  else:
    form = RegistrationForm()
  
  context = {'form': form}
  return render(request, 'pages/sign-up.html', context)


class UserPasswordResetView(auth_views.PasswordResetView):
  template_name = 'accounts/forgot-password.html'
  form_class = UserPasswordResetForm


class UserPasswordResetConfirmView(auth_views.PasswordResetConfirmView):
  template_name = 'accounts/recover-password.html'
  form_class = UserSetPasswordForm


class UserPasswordChangeView(auth_views.PasswordChangeView):
  template_name = 'accounts/password_change.html'
  form_class = UserPasswordChangeForm


def user_logout_view(request):
  logout(request)
  return redirect('/accounts/login/')