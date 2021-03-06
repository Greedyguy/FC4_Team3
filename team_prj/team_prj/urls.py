"""team_prj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

from random_board.urls import urlpatterns as rpost_url
from django.views.generic import TemplateView

from django.contrib.auth.views import login as django_login
from django.contrib.auth.views import logout as django_logout


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^rpost/', include(rpost_url, namespace='rpost')),
    url(
        r'^login/$', django_login,
        {'template_name': 'login.html'}, name="login_url"
    ),
    url(
        r'^logout/$', django_logout,
        {'next_page': '/login/'}, name="logout_url"
    ),
    url(
        r'^signup/$', 'profiles.views.signup', name='signup'
    ),
    url(
        r'^signup_ok/$',
        TemplateView.as_view(template_name='signup_ok.html'),
        name='signup_ok'),
]
