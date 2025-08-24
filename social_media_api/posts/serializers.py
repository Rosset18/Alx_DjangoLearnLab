from rest_framework import serializers
from accounts.serializers import CustomUserSerializer
from .models import Post, Comment

class PostSerializer(serializers.ModelSerializer):
    # author = CustomUserSerializer()
    class Meta:
        model = Post
        fields = ['title', 'content', 'author', 'created_at', 'updated_at']
        read_only_fields = ['author']

    def create(self, validated_data):
        request = self.context.get('request')
        print(request.data)

        validated_data['author'] = request.user
        
        # post = Post.objects.create(**validated_data)
        return super().create(**validated_data)
    
class CommentSerializer(serializers.ModelSerializer):
    author = CustomUserSerializer()
    post = PostSerializer()

    class Meta:
        model = Comment
        fields = ['author', 'post', 'content', 'created_at', 'updated_at']

    def create(self, validated_data):
        pass
