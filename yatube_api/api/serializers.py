from posts.models import Comment, Group, Post
from rest_framework import serializers


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ('id', 'title', 'slug', 'description')


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(read_only=True,
                                          slug_field='username')

    group = serializers.SlugRelatedField(required=False,
                                         queryset=Group.objects.all(),
                                         slug_field='slug'
                                         )

    class Meta:
        model = Post
        fields = ('id', 'text', 'author', 'pub_date', 'group', 'image')
        read_only_fields = ('author', 'id')


class CommentSerializer(serializers.ModelSerializer):
    post = serializers.PrimaryKeyRelatedField(read_only=True)

    author = serializers.SlugRelatedField(read_only=True,
                                          slug_field='username')

    class Meta:
        model = Comment
        fields = ('id', 'author', 'post', 'text', 'created')
        read_only_fields = ('author', 'id')
