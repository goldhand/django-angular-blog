from django.conf.urls import patterns, include, url
from rest_framework import routers

from blog.views import PostViewSet, CategoryViewSet, PostList, PostDetail
from users.views import UserViewSet


router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'users', UserViewSet)

urlpatterns = patterns('',
                       # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
                       # url(r'^admin/', include(admin.site.urls)),
                       url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
                       url(r'^angular/partials/post-list/', 'blog.views.angular_view_post_list'),
                       url(r'^angular/partials/post-detail/', 'blog.views.angular_view_post_detail'),
                       #url(r'^', include('blog.urls')),
                       #url(r'^', include(router.urls)),
                       url(r'^', include(router.urls)),
)
