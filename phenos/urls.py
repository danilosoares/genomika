from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.login, name='login'),
    url(r'^index/$', views.index, name='index'),
    url(r'^results/$', views.results, name='results'),
    url(r'^diseases/$', views.diseases, name='diseases'),
    url(r'^auth/$', views.authenticate, name='authenticate'),
]