from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.template import Context
from phenos.models import Disease

# Create your views here.

def index(request):
    template = loader.get_template('phenos/index.html')
    return HttpResponse(template.render(request))

def results(request):
	term = request.GET['term']
	
	disease = Disease.objects.get(name=term)

	print(disease)

	template = loader.get_template('phenos/results.html')
	c = Context({'genes' : genes, 'term' : term, 'disease' : disease })
	return HttpResponse(template.render(c))