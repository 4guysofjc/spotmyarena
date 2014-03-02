from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from spotmyarena import views
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'spotmyarena.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

     url(r'^index/$', views.indexView),
     url(r'^search/$', views.searchResultsView),
     url(r'^club/$', views.clubProfile),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('django.contrib.staticfiles.views',
        url(r'^static/(?P<path>.*)$', 'serve'),
    ) 
