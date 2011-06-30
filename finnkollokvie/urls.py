from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'finnkollokvie.views.home', name='home'),
    # url(r'^finnkollokvie/', include('finnkollokvie.foo.urls')),
    (r'^kollokvier/$', 'kollokvier.views.add'),
    (r'^list/$', 'kollokvier.views.list'),
    #(r'^kollokvier/(?P<student_id>\d+)/$', 'kollokvier.views.list'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
