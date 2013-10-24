from django.conf.urls import patterns, include, url
from rest_framework import routers

from blog.views import PostViewSet, UserViewSet, CategoryViewSet, PostList, PostDetail

from essays.views import IntroViewSet, BodyViewSet, ConclusionViewSet, EssayViewSet


router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'intro', IntroViewSet)
router.register(r'body', BodyViewSet)
router.register(r'conclusion', ConclusionViewSet)
router.register(r'essay', EssayViewSet)
router.register(r'users', UserViewSet)

urlpatterns = patterns('',
                       # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
                       # url(r'^admin/', include(admin.site.urls)),
                       url(r'^$', 'blog.views.angular_view'),
                       url(r'^api/', include(router.urls)),
                       url(r'^api/api-auth/', include('rest_framework.urls', namespace='rest_framework')),
                       url(r'^posts', include('blog.urls', namespace='posts')),
                       url(r'^buildbooth/$', 'essays.views.angular_view'),
                       #url(r'^', include('blog.urls')),
                       #url(r'^', include(router.urls)),
)

urlpatterns += patterns('essays.views',
                        url(r'^api/angular/partials/essay-list/', 'angular_view_essay_list'),
                        url(r'^api/angular/partials/essay-detail/', 'angular_view_essay_detail'),
                        url(r'^api/angular/partials/essay-document/', 'angular_view_essay_document'),
                        )

urlpatterns += patterns('blog.views',
                       url(r'^api/angular/partials/post-list/', 'angular_view_post_list'),
                       url(r'^api/angular/partials/post-detail/', 'angular_view_post_detail'),
                       )
