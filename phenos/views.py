from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.template import Context
from django.core import serializers
from phenos.models import Disease
from phenos.models import Gene
from phenos.models import User

# Create your views here.

def index(request):
	if not request.session["user_id"]:
  		template = loader.get_template('phenos/login.html')
		return HttpResponse(template.render(request))
   
	template = loader.get_template('phenos/index.html')
	return HttpResponse(template.render(request))

def results(request):
	if not request.session["user_id"]:
		template = loader.get_template('phenos/login.html')
		return HttpResponse(template.render(request))
	term = request.GET['term']
	diseases = Disease.objects.filter(name__in=term.split(','))
	
	template = loader.get_template('phenos/results.html')
	c = Context({'term' : term, 'diseases' : diseases })
	return HttpResponse(template.render(c))

def diseases(request):
	if not request.session["user_id"]:
		template = loader.get_template('phenos/login.html')
		return HttpResponse(template.render(request))
	term = request.GET['term']

	diseases = Disease.objects.filter(name__contains=term)
	data = serializers.serialize('json', diseases)
	return HttpResponse(data, content_type='application/json')

def login(request):
	template = loader.get_template('phenos/login.html')
	return HttpResponse(template.render(request))

def authenticate(request):
    if request.method != 'POST':
        raise Http404('Only POSTs are allowed')
    try:
        user = User.objects.get(email=request.POST['email'])
        if user.password == request.POST['password']:
            request.session['user_id'] = user.id
            template = loader.get_template('phenos/index.html')
    	return HttpResponse(template.render(request))
    except Member.DoesNotExist:
        template = loader.get_template('phenos/login.html')
	return HttpResponse(template.render(request))

def logout(request):
	try:
		del request.session['user_id']
	except KeyError:
		pass
	template = loader.get_template('phenos/login.html')
	return HttpResponse(template.render(request))

