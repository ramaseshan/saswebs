from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sabwebs.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^select2/', include('django_select2.urls')),
    url(r'^$', 'sabwebs.views.home', name='home'),
    url(r'^search/(?P<prod_id>[-\w]+)$', 'sabwebs.views.home', name='home'),
    url(r'^get_products/$', 'sabwebs.views.get_products', name='get_products'),
)
import debug_toolbar
urlpatterns += patterns('',
    url(r'^__debug__/', include(debug_toolbar.urls)),
)
