from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sabwebs.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^select2/', include('django_select2.urls')),
    url(r'^$', 'sabwebs.views.home', name='home'),
    url(r'^search/(?P<prod_id>[-\w]+)$', 'sabwebs.views.home', name='home'),
    url(r'^get_products/$', 'sabwebs.views.get_products', name='get_products'),
    url(r'^add_like_product/$','sabwebs.views.do_like',name="do_like"),
    url(r'^undo_like_product/$','sabwebs.views.undo_like',name="do_like"),
)
