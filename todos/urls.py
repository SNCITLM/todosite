from django.conf.urls import url

from . import views
app_name = 'todos'
urlpatterns = [
    url(r'^index', views.index, name='index'),
    url(r'^about', views.about, name='about'),
    url(r'^(?P<todo_id>[0-9]+)/edit', views.edit, name='edit'),
    url(r'^(?P<todo_id>[0-9]+)/save', views.save, name='save'),
    url(r'^(?P<todo_id>[0-9]+)/delete', views.delete, name='delete'),
]
