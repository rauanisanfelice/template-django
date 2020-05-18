from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import View, DeleteView

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import SignUpForm

import datetime
import json

import logging
logger = logging.getLogger(__name__)

########################################################################
def bad_request(request, exeption):
    context = {}
    return render(request, 'error.html', context, status=400)

def permission_denied(request, exeption):
    context = {}
    return render(request, 'error.html', context, status=403)

def page_not_found(request, exeption):
    context = {}
    return render(request, 'error.html', context, status=404)

def server_error(request):
    context = {}
    return render(request, 'error.html', context, status=500)

########################################################################
@login_required
def index(request):
    return redirect('login')

class SignUp(generic.CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('home')
    template_name = 'signup.html'

class Home(View):
    template_name = 'home.html'

    def get(self, request):
        return render(request, self.template_name)