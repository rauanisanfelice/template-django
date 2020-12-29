from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import View, DeleteView

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import SignUpForm

from decouple import config

import datetime
import json
import requests

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
def keepalive(request):
    html = "<html><body>KeepAlive Ok.</body></html>"
    return HttpResponse(html)


def GetVersion():
    GIT_USUARIO = config('GIT_USUARIO')
    GIT_USUARIO_TOKEN = config('GIT_USUARIO_TOKEN')
    repositorio = ''
    try:
        r = requests.get('https://api.github.com/repos/{GIT_USUARIO}/{repositorio}/tags', auth=(GIT_USUARIO, GIT_USUARIO_TOKEN))
        if r.status_code == 200:
            retorno = r.json()
            return retorno[0]['name'] if retorno else '0.0.0'
        else:
            logger.error(f'Erro ao buscar versão do repositório')
            return '0.0.0'
    except:
        logger.error(f'Erro ao buscar versão do repositório')
        return '0.0.0'


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