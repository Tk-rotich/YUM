from django.shortcuts import render
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView
from django.views.generic.base import TemplateView
from django.contrib.auth.models import User
from .forms import userCommentsForm
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from userfeedback.models import userComments
from django.shortcuts import redirect
from django import forms

# Create your views here.

class IndexView(SuccessMessageMixin, CreateView):
    model = userComments
    form_class = userCommentsForm
    template_name = "userfeedback/comments.html"
    success_url= 'success'
    success_message = "Comment Submited Successfully. Thank you for taking time to get to us"


    def form_valid(self, form):
        form.instance.name = self.request.user
        return super().form_valid(form)
   

class SuccessView(TemplateView):
    template_name = "userfeedback/success.html"

class RegisterView(CreateView):
    model = User
    fields = ['username','password']
    template_name = 'registration/register.html'
    success_url = '/accounts/login/'


def logout(request):
    auth.logout(request)
    return redirect('/accounts/login/')

def log(request):
    return redirect('/')