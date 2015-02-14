from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tictactoeproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include('tictactoe.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
