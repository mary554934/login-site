from django.urls import path
from . import views

urlpatterns = [
    url(r'^logout/$', logout, {'template_name': 'index.html'}, name='logout')
]