from rest_framework import serializers

from posts.models import Comment, Group, Post


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ('__all__')


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(read_only=True,
                                          slug_field='username')

    group = serializers.SlugRelatedField(required=False,
                                         queryset=Group.objects.all(),
                                         slug_field='slug'
                                         )

    class Meta:
        model = Post
        fields = ('__all__')
        read_only_fields = ('author', 'id')


class CommentSerializer(serializers.ModelSerializer):
    post = serializers.PrimaryKeyRelatedField(read_only=True)

    author = serializers.SlugRelatedField(read_only=True,
                                          slug_field='username')

    class Meta:
        model = Comment
        fields = ('__all__')
        read_only_fields = ('author', 'id')
