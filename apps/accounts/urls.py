from django.conf.urls import url, include
from django.contrib.auth.views import login, logout
from . import views

urlpatterns = [
    url(r'^profile/$', views.profile, name='accounts_profile'),
    url(r'^login/$', login, kwargs={'template_name':'accounts/login.html'}, name='accounts_login'),
    url(r'^logout/$', logout, kwargs={'next_page':'/'}, name='accounts_logout'),

]
