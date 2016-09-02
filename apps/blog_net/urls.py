from django.conf.urls import url, include
from django.contrib.auth.views import login, logout
from . import views
from feeds import ArchiveFeed

from django.contrib.sitemaps.views import sitemap
from sitemaps import BlogSitemap, SiteSitemap

from django.contrib.flatpages import views as flat_views

sitemaps = {
    'blog': BlogSitemap,
    'pages': SiteSitemap(['contact', 'archive'])
}

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^archive/$', views.archive, name='archive'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^profile/$', views.profile, name='profile')

]

urlpatterns += [
    url(r'^login/$', login, kwargs={'template_name':'blog_net/login.html'}, name='login'),
    url(r'^logout/$', logout, kwargs={'next_page':'/'}, name='logout'),

    url(r'^feed/archive/$', ArchiveFeed()),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps},name='django.contrib.sitemaps.views.sitemap'),
    url(r'^about/$', flat_views.flatpage, {'url': '/about/'}, name='about'),

]
