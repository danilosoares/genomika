from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.template import Context
from phenos.models import Disease
from phenos.models import Gene

# Create your views here.

def index(request):
    template = loader.get_template('phenos/index.html')
    return HttpResponse(template.render(request))

def results(request):
	term = request.GET['term']
	
	diseases = Disease.objects.filter(name__contains=term)

	template = loader.get_template('phenos/results.html')
	c = Context({'term' : term, 'diseases' : diseases })
	return HttpResponse(template.render(c))