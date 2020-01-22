from django.conf import settings
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, resolve_url
from django.views.generic import CreateView
from .forms import SignupForm

@login_required
def profile(request):
    request.user
    # request.user
    # logout: django.contrib.auth.models.AnonymousUser
    # login: django.contrib.auth.models.User

    return render(request, 'accounts/profile.html')


class SignupView(CreateView):
    model = User
    form_class = SignupForm
    template_name = 'accounts/signup.html'

    def get_success_url(self):
        return resolve_url('profile')

    def form_valid(self, form):
        user = form.save()
        auth_login(self.request, user)
        return redirect(self.get_success_url())

signup = SignupView.as_view()