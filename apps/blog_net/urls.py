from django.conf.urls import url
from . import views
from feeds import ArchiveFeed


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^archive/$', views.archive, name='archive'),
    url(r'^contact/$', views.contact, name='contact'),

]

urlpatterns += [
    url(r'^feed/archive/$', ArchiveFeed()),
]
