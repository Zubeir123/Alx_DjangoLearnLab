from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect

from .forms import RegistrationForm, UserUpdateForm, ProfileForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import PostForm
from .models import Post


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

# LIST
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'   # default: <app>/<model>_list.html
    context_object_name = 'posts'
    paginate_by = 5  # optional

# DETAIL
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html' # default: <app>/<model>_detail.html
    context_object_name = 'post'

# CREATE
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, 'Post created successfully.')
        return super().form_valid(form)

# UPDATE (only author can edit)
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def test_func(self):
        return self.get_object().author == self.request.user

    def handle_no_permission(self):
        messages.error(self.request, "You don't have permission to edit this post.")
        return super().handle_no_permission()

    def form_valid(self, form):
        messages.success(self.request, 'Post updated successfully.')
        return super().form_valid(form)

# DELETE (only author can delete)
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('post-list')

    def test_func(self):
        return self.get_object().author == self.request.user

    def handle_no_permission(self):
        messages.error(self.request, "You don't have permission to delete this post.")
        return super().handle_no_permission()
