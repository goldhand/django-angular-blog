from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework import permissions, viewsets

from .models import Post, Category
from .serializers import PostSerializer, UserSerializer, CategorySerializer
from .permissions import IsOwnerOrReadOnly


class PostViewSet(viewsets.ModelViewSet):
    """
	This viewset automatically provides 'list', 'create', 'retrieve',
	'update', and 'destroy' actions.
	"""
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

    def pre_save(self, obj):
        obj.owner = self.request.user


class CategoryViewSet(viewsets.ModelViewSet):
    """
	This viewset automatically provides 'list', 'create', 'retrieve',
	'update', and 'destroy' actions.
	"""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
	This viewset automatically provides 'list' and 'detail' actions.
	"""
    queryset = User.objects.all()
    serializer_class = UserSerializer


def angular_view(request):
    return render(request, 'blog/angular/index.html')


def angular_view_post_list(request):
    return render(request, 'blog/angular/partials/post-list.html')


def angular_view_post_detail(request):
    return render(request, 'blog/angular/partials/post-detail.html')





