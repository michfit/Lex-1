from django.urls import path
from django.conf.urls import include, url
import users
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    url(r'^select2/', include('django_select2.urls')),
    url(r'^profile/(?P<pk>\d+)/$', users.views.profile, name='profile_with_pk'),
    url(r'^connect/(?P<operation>.+)/(?P<pk>\d+)/$', users.views.change_friends, name='change_friends')
]
