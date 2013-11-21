from rest_framework import serializers

from .models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    posts = serializers.HyperlinkedRelatedField(many=True, view_name='post-detail')
    essays = serializers.HyperlinkedRelatedField(many=True, view_name='essay-detail', read_only=True)

    class Meta:
        model = User
        fields = ('id', 'url', 'username', 'posts', 'essays')


