from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
]
