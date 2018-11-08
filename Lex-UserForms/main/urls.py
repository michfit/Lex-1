from django.urls import path
from django.conf.urls import include, url

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^select2/', include('django_select2.urls')),
]
