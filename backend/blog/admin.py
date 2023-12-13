from django.contrib import admin
from .models import Post, Tag


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'publish_status', 'publish_date', 'date_updated']
    list_filter = ['tag', 'publish_status',]
    search_fields = ('title', 'body')
    
     
        
class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'date_created',]
    list_filter = ['name']
    search_fields = ('name',)
    

admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)