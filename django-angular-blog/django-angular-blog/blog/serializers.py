from django.contrib.auth.models import User

from rest_framework import serializers

from .models import Post, Category


class PostSerializer(serializers.HyperlinkedModelSerializer):
    categories = serializers.HyperlinkedRelatedField(many=True, view_name='category-detail')
    owner = serializers.Field(source='owner.username')
    _next = serializers.SerializerMethodField('get_next')
    _previous = serializers.SerializerMethodField('get_previous')

    class Meta:
        model = Post
        fields = (
            'id', 'url', 'created', 'owner', 'title', 'content', 'categories', 'related_posts', '_next', '_previous'
        )

    def get_next(self, obj):
        try:
            return obj.get_next_by_created().get_display_url()
        except Post.DoesNotExist:
            return Post.objects.reverse().latest('created').get_display_url()
        except AttributeError:
            return None

    def get_previous(self, obj):
        try:
            return obj.get_previous_by_created().get_display_url()
        except Post.DoesNotExist:
            return Post.objects.latest('created').get_display_url()
        except AttributeError:
            return None


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    posts = serializers.HyperlinkedRelatedField(many=True, view_name='post-detail')

    class Meta:
        model = Category
        fields = ('id', 'title', 'url', 'posts')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    posts = serializers.HyperlinkedRelatedField(many=True, view_name='post-detail')

    class Meta:
        model = User
        fields = ('url', 'username', 'posts')
