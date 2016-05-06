from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<todo_id>[0-9]+)/edit$', views.edit, name='edit'),
]
