from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about$', views.about, name='about'),
    url(r'^(?P<todo_id>[0-9]+)/edit$', views.edit, name='edit'),
]
