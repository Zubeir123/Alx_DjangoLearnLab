from django.contrib import messages
from django.contrib.auth import login
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect

from .forms import RegistrationForm, UserUpdateForm, ProfileForm

# --- Auth Views using built-ins for login/logout ---

class UserLoginView(LoginView):
    template_name = 'registration/login.html'  # we will create this

class UserLogoutView(LogoutView):
    template_name = 'registration/logged_out.html'  # optional

# --- Simple home page (optional) ---

def home(request):
    return render(request, 'blog/home.html')


# --- Registration ---

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Your account was created successfully.')
            login(request, user)  # auto-login after registration
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = RegistrationForm()
    return render(request, 'blog/register.html', {'form': form})

# --- Profile view/edit ---

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Profile updated.')
            return redirect('profile')
        else:
            messages.error(request, 'Please fix the errors below.')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileForm(instance=request.user.profile)
    return render(request, 'blog/profile.html', {'u_form': u_form, 'p_form': p_form})

#
# def pos_page(request):
#     return HttpResponse("<h1>This is the POS page</h1>")