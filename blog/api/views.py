from .serializers import PostSerializer, TagSerializer
from rest_framework import mixins, generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter, OrderingFilter
from ..models import Post, Tag

# page size
class SetBlogPostPaginationResult(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 1000

class PostViewSet(generics.GenericAPIView, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    serializer_class = PostSerializer
    queryset = Post.objects.all().filter(publish_status=True)
    lookup_field = 'slug'
    pagination_class = SetBlogPostPaginationResult
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', 'body', 'author__username', 'tag__name', ]

    def get(self, request, slug=None):
        if slug:
            return self.retrieve(request)
        else:
            return self.list(request)
        
        
class TagViewSet(generics.GenericAPIView, mixins.ListModelMixin):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()
    
    def get(self, request):
        return self.list(request)
    
    
    
class TagFilterPostViewSet(generics.GenericAPIView, mixins.ListModelMixin):    
    serializer_class = PostSerializer
    queryset = Post.objects.all().filter(publish_status=True)
    lookup_field = 'id'
    pagination_class = SetBlogPostPaginationResult
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', 'body', 'author__username', 'tag__name', ]
    
    
    def get_queryset(self):
        tag_slug = self.kwargs.get('tag', None)
        if tag_slug:
            queryset = self.queryset.filter(tag=tag_slug)
        return queryset

    def get(self, request, tag=None):
        return self.list(request)
        