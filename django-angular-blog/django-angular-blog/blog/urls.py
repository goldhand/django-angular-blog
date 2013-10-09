from django.conf.urls import patterns, url, include
from rest_framework.routers import DefaultRouter

from .views import PostList, PostDetail



urlpatterns = patterns('blog.views',
                       url(r'^$', PostList.as_view(), name='list'),
                       url(r'^/(?P<pk>\d+)$', PostDetail.as_view(), name='detail'),
)

