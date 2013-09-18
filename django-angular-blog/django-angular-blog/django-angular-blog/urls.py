from django.conf.urls import patterns, include, url
from rest_framework import routers


urlpatterns = patterns('',
                       # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
                       # url(r'^admin/', include(admin.site.urls)),
                       url(r'^api/', include('blog.urls')),
                       url(r'^$', 'blog.views.angular_view'),
                       #url(r'^', include(router.urls)),
)
