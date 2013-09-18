from django.conf.urls import patterns, url, include
from rest_framework.routers import DefaultRouter

from .views import PostViewSet, UserViewSet, CategoryViewSet


# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'users', UserViewSet)

urlpatterns = patterns('blog.views',
                       url(r'^', include(router.urls)),
                       url(r'^angular/partials/post-list/', 'angular_view_post_list'),
                       url(r'^angular/partials/post-detail/', 'angular_view_post_detail'),
                       url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)

