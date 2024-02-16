from rest_framework import serializers
from ..models import Post, Tag

class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields= '__all__'

class PostSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.username', read_only=True)
    #tag = serializers.SerializerMethodField(read_only=True)
    abssolute_url = serializers.SerializerMethodField('get_absolute_url')

    class Meta:
        model = Post
        fields = ['title', 'slug', 'body', 'image', "abssolute_url", 'tag', 'author', 'date_updated', "publish_status", "publish_date"]
        
    
    def get_absolute_url(self, obj):
        return obj.get_absolute_url()