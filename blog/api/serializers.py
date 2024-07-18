from rest_framework import serializers
from bs4 import BeautifulSoup
from ..models import Post, Tag

class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields= '__all__'

class PostSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.username', read_only=True)
    #tag = serializers.SerializerMethodField(read_only=True)
    abssolute_url = serializers.SerializerMethodField('get_absolute_url')
    tag = serializers.SerializerMethodField('get_tag')
    truncated_body = serializers.SerializerMethodField('get_truncated_body')

    class Meta:
        model = Post
        fields = ['title', 'slug', 'truncated_body', 'image', "abssolute_url", 'tag', 'author', 'date_updated', "publish_status", "publish_date"]
        
    
    def get_absolute_url(self, obj):
        return obj.get_absolute_url()
    
    def get_tag(self, obj):
        tag_list=[]
        for item in obj.tag.all():
            tg = {
                'name':item.name,
                'id':item.id
            }
            tag_list.append(tg)
        return tag_list
    
    def get_truncated_body(self, obj):
        return self.truncate_html(obj.body, 100)

    def truncate_html(self, html, length):
        # Use BeautifulSoup to parse the HTML and get the plain text
        soup = BeautifulSoup(html, "html.parser")
        text = soup.get_text()

        # Truncate the text to the desired length
        if len(text) <= length:
            return text
        truncated_text = text[:length] + '...'
        return truncated_text
    

class SinglePostSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.username', read_only=True)
    #tag = serializers.SerializerMethodField(read_only=True)
    abssolute_url = serializers.SerializerMethodField('get_absolute_url')
    tag = serializers.SerializerMethodField('get_tag')

    class Meta:
        model = Post
        fields = ['title', 'slug', 'body', 'image', "abssolute_url", 'tag', 'author', 'date_updated', "publish_status", "publish_date"]
        
    
    def get_absolute_url(self, obj):
        return obj.get_absolute_url()
    
    def get_tag(self, obj):
        tag_list=[]
        for item in obj.tag.all():
            tg = {
                'name':item.name,
                'id':item.id
            }
            tag_list.append(tg)
        return tag_list
    

class RelatedPostSerializer(serializers.ModelSerializer):
    abssolute_url = serializers.SerializerMethodField('get_absolute_url')

    class Meta:
        model = Post
        fields = ['title', 'slug', 'image', "abssolute_url",]
        
    
    def get_absolute_url(self, obj):
        return obj.get_absolute_url()
    