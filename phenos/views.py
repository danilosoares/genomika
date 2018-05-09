# -*- coding: utf-8 -*-

from django.template.response import TemplateResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.template import Context
from django.core import serializers
from phenos.models import Disease
from phenos.models import Gene
from phenos.models import User
from django import forms

# Create your views here.


def index(request):
    if 'user_id' not in request.session:
        template = loader.get_template('phenos/login.html')
        return HttpResponse(template.render({}, request))

    template_name = 'phenos/index.html'
    return TemplateResponse(request, template_name)


def results(request):
    if 'user_id' not in request.session:
        template = loader.get_template('phenos/login.html')
        return HttpResponse(template.render({}, request))
    term = request.POST['term']
    diseases = Disease.objects.filter(name__in=term.split(','))

    template_name = 'phenos/results.html'
    c = {'term': term, 'diseases': diseases}
    return TemplateResponse(request, template_name, c)


def diseases(request):
    if 'user_id' not in request.session:
        template = loader.get_template('phenos/login.html')
        return HttpResponse(template.render({}, request))
    term = request.GET['term']

    diseases = Disease.objects.filter(name__contains=term)
    data = serializers.serialize('json', diseases)
    return HttpResponse(data, content_type='application/json')


def login(request):
    if 'user_id' not in request.session:
        template = loader.get_template('phenos/login.html')
        return HttpResponse(template.render({}, request))
    template = loader.get_template('phenos/index.html')
    return HttpResponse(template.render({}, request))


def registration(request):
    template = loader.get_template('phenos/registration.html')
    return HttpResponse(template.render({}, request))


def user_create(request):
    email = request.POST['user_email']
    if not email:
        raise forms.ValidationError("Email não pode ficar em branco!")
    if not email.find('@'):
        raise forms.ValidationError(
            "Use um email válido para criar o usuário!")
    if not request.POST['user_password']:
        raise forms.ValidationError("Senha não pode ficar em branco!")

    user_email = request.POST['user_email']
    user_password = request.POST['user_password']
    user = User(email=user_email, password=user_password)
    user.save()
    request.session['user_id'] = user.id
    template = loader.get_template('phenos/index.html')
    return HttpResponse(template.render({}, request))


def authenticate(request):
    if request.method != 'POST':
        raise Http404('Only POSTs are allowed')
    try:
        user = User.objects.get(email=request.POST['user_email'])
        template = loader.get_template('phenos/index.html')
        if user.password == request.POST['user_password']:
            request.session['user_id'] = user.id
        return HttpResponse(template.render({}, request))
    except User.DoesNotExist:
        template = loader.get_template('phenos/login.html')
        return HttpResponse(template.render({}, request))


def logout(request):
    try:
        del request.session['user_id']
    except KeyError:
        pass
    template = loader.get_template('phenos/login.html')
    return HttpResponse(template.render({}, request))
