from rest_framework import serializers
from .models import Author, Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"


        
class AuthorSerializer(serializers.ModelSerializer):
    posts = PostSerializer(many=True, read_only=True)
    class Meta:
        model = Author
        fields = "__all__"
        
        
# class PostSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Post
#         fields = "__all__"


        
# class AuthorSerializer(serializers.HyperlinkedModelSerializer):
#     posts = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name="post-detail")
#     class Meta:
#         model = Author
#         fields = "__all__"