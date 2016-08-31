from django.conf.urls import url
from . import views
from feeds import ArchiveFeed

from django.contrib.sitemaps.views import sitemap
from sitemaps import BlogSitemap, SiteSitemap

sitemaps = {
    'blog': BlogSitemap,
    'pages': SiteSitemap(['contact', 'archive'])
}

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^archive/$', views.archive, name='archive'),
    url(r'^contact/$', views.contact, name='contact'),

]

urlpatterns += [
    url(r'^feed/archive/$', ArchiveFeed()),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps},name='django.contrib.sitemaps.views.sitemap'),

]
