from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^about/', views.about, name='about'),
    url(r'^index', views.index, name='index'),
    url(r'^(?P<todo_id>[0-9]+)/edit$', views.edit, name='edit'),
    url(r'^.*$', views.index, name='index'),
]
