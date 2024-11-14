from django.shortcuts import render, redirect
from admin_material.forms import LoginForm, RegistrationForm, UserPasswordResetForm, UserSetPasswordForm, UserPasswordChangeForm
from django.contrib.auth import logout
from django.contrib.auth import views as auth_views

# Create your views here.


def index(request):
    context = {
        'segment': 'dashboard',
        'parent': 'home'
    }
    return render(request, 'pages/index.html', context)

def colors(request):
    context = {
        'segment': 'colors',
        'parent': 'theme'
    }
    return render(request, 'pages/colors.html', context)


def typography(request):
    context = {
        'segment': 'typography',
        'parent': 'theme'
    }
    return render(request, 'pages/typography.html', context)

# base
def accordion(request):
   context = {
        'segment': 'accordion',
        'parent': 'base'
    }
   return render(request, 'base/accordion.html', context)

def breadcrumb(request):
   context = {
        'segment': 'breadcrumb',
        'parent': 'base'
    }
   return render(request, 'base/breadcrumb.html', context)

def cards(request):
   context = {
        'segment': 'cards',
        'parent': 'base'
    }
   return render(request, 'base/cards.html', context)

def carousel(request):
   context = {
        'segment': 'carousel',
        'parent': 'base'
    }
   return render(request, 'base/carousel.html', context)

def collapse(request):
   context = {
        'segment': 'collapse',
        'parent': 'base'
    }
   return render(request, 'base/collapse.html', context)

def list_group(request):
   context = {
        'segment': 'list_group',
        'parent': 'base'
    }
   return render(request, 'base/list-group.html', context)

def navs_tabs(request):
   context = {
        'segment': 'navs_tabs',
        'parent': 'base'
    }
   return render(request, 'base/navs-tabs.html', context)

def pagination(request):
   context = {
        'segment': 'pagination',
        'parent': 'base'
    }
   return render(request, 'base/pagination.html', context)

def placeholders(request):
   context = {
        'segment': 'placeholders',
        'parent': 'base'
    }
   return render(request, 'base/placeholders.html', context)

def popovers(request):
   context = {
        'segment': 'popovers',
        'parent': 'base'
    }
   return render(request, 'base/popovers.html', context)

def progress(request):
   context = {
        'segment': 'progress',
        'parent': 'base'
    }
   return render(request, 'base/progress.html', context)

def spinners(request):
   context = {
        'segment': 'spinners',
        'parent': 'base'
    }
   return render(request, 'base/spinners.html', context)

def base_tables(request):
   context = {
        'segment': 'tables',
        'parent': 'base'
    }
   return render(request, 'base/tables.html', context)

def tooltips(request):
   context = {
        'segment': 'tooltips',
        'parent': 'base'
    }
   return render(request, 'base/tooltips.html', context)



# Buttons
def button_group(request):
   context = {
        'segment': 'button_group',
        'parent': 'buttons'
    }
   return render(request, 'buttons/button-group.html', context)

def buttons(request):
   context = {
        'segment': 'buttons',
        'parent': 'buttons'
    }
   return render(request, 'buttons/buttons.html', context)

def dropdowns(request):
   context = {
        'segment': 'dropdowns',
        'parent': 'buttons'
    }
   return render(request, 'buttons/dropdowns.html', context)


# Charts
def charts(request):
   context = {
      'segment': 'charts',
      'parent': 'home'
   }
   return render(request, 'pages/charts.html', context)


# Forms
def check_radios(request):
   context = {
        'segment': 'check_radios',
        'parent': 'forms'
    }
   return render(request, 'forms/checks-radios.html', context)

def floating_labels(request):
   context = {
        'segment': 'floating_labels',
        'parent': 'forms'
    }
   return render(request, 'forms/floating-labels.html', context)

def form_control(request):
   context = {
        'segment': 'form_control',
        'parent': 'forms'
    }
   return render(request, 'forms/form-control.html', context)

def input_group(request):
   context = {
        'segment': 'input_group',
        'parent': 'forms'
    }
   return render(request, 'forms/input-group.html', context)

def layout(request):
   context = {
        'segment': 'layout',
        'parent': 'forms'
    }
   return render(request, 'forms/layout.html', context)

def range(request):
   context = {
        'segment': 'range',
        'parent': 'forms'
    }
   return render(request, 'forms/range.html', context)

def select(request):
   context = {
        'segment': 'select',
        'parent': 'forms'
    }
   return render(request, 'forms/select.html', context)

def validation(request):
   context = {
        'segment': 'validation',
        'parent': 'forms'
    }
   return render(request, 'forms/validation.html', context)


# Icons
def icons_brand(request):
   context = {
        'segment': 'icons_brand',
        'parent': 'icons'
    }
   return render(request, 'icons/coreui-icons-brand.html', context)

def icons_flag(request):
   context = {
        'segment': 'icons_flag',
        'parent': 'icons'
    }
   return render(request, 'icons/coreui-icons-flag.html', context)

def icons_free(request):
   context = {
        'segment': 'icons_free',
        'parent': 'icons'
    }
   return render(request, 'icons/coreui-icons-free.html', context)


# Notifications
def alerts(request):
   context = {
      'segment': 'alerts',
      'parent': 'notifications'
   }
   return render(request, 'notifications/alerts.html', context)

def badge(request):
   context = {
      'segment': 'badge',
      'parent': 'notifications'
   }
   return render(request, 'notifications/badge.html', context)

def modals(request):
   context = {
      'segment': 'modals',
      'parent': 'notifications'
   }
   return render(request, 'notifications/modals.html', context)

def toasts(request):
   context = {
      'segment': 'toasts',
      'parent': 'notifications'
   }
   return render(request, 'notifications/toasts.html', context)

# Widgets
def widgets(request):
   context = {
      'segment': 'widgets',
      'parent': 'home'
   }
   return render(request, 'pages/widgets.html', context)

#########

class UserLoginView(auth_views.LoginView):
  template_name = 'accounts/login.html'
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
  return render(request, 'accounts/register.html', context)


def error_404(request):
   return render(request, 'accounts/404.html')

def error_500(request):
   return render(request, 'accounts/500.html')

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
