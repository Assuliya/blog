from django.conf.urls import url, include
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
    url(r'^$', views.index, name='blog_index'),
    url(r'^archive/$', views.archive, name='blog_archive'),
    url(r'^contact/$', views.contact, name='blog_contact'),

]

urlpatterns += [
    url(r'^feed/archive/$', ArchiveFeed()),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps},name='django.contrib.sitemaps.views.sitemap'),
    url(r'^about/$', flat_views.flatpage, {'url': '/about/'}, name='blog_about'),

]
