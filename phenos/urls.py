from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^index/$', views.index, name='index'),
    url(r'^results/$', views.results, name='results'),
    url(r'^diseases/$', views.diseases, name='diseases'),
    url(r'^auth/$', views.authenticate, name='authenticate'),
    url(r'^registration/$', views.registration, name='registration'),
    url(r'^user_create/$', views.user_create, name='user_create'),
]