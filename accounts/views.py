from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from django.contrib.auth.models import User
from django.views.generic import CreateView

@login_required
def profile(request):
    request.user
    return render(request, 'accounts/profile.html')

signup = CreateView.as_view(model=User,form_class=UserCreationForm,success_url=settings.LOGIN_URL,template_name='accounts/signup.html')