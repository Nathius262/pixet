from .serializers import PostSerializer, TagSerializer, RelatedPostSerializer, SinglePostSerializer
from rest_framework import mixins, generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter, OrderingFilter
from ..models import Post, Tag
from hitcount.models import HitCount
from hitcount.views import HitCountMixin
from rest_framework.response import Response
from django.db.models import Count

# page size
class SetBlogPostPaginationResult(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 1000


class PostViewSet(generics.GenericAPIView, mixins.ListModelMixin, mixins.RetrieveModelMixin, HitCountMixin):
    queryset = Post.objects.all().filter(publish_status=True)
    lookup_field = 'slug'
    pagination_class = SetBlogPostPaginationResult
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', 'body', 'author__username', 'tag__name']

    def get_serializer_class(self):
        if self.kwargs.get('slug') is not None:
            return SinglePostSerializer
        return PostSerializer

    def get(self, request, slug=None):
        if slug:
            response = self.retrieve(request)
            # Increment the hit count
            post = self.get_object()
            hit_count = HitCount.objects.get_for_object(post)
            self.hit_count(request, hit_count)
            
            # Get related posts
            related_posts = Post.objects.filter(tag__in=post.tag.all()).exclude(slug=post.slug)
            related_posts = related_posts.annotate(tag_count=Count('tag')).order_by('-tag_count', '-publish_date')[:4]

            # Serialize the related posts
            related_posts_serializer = RelatedPostSerializer(related_posts, many=True)
            
            # Add related posts to the response data
            response_data = response.data
            response_data['related_posts'] = related_posts_serializer.data
            session_id = request.session.session_key
            response_data['session_id'] = session_id
            return Response(response_data)
        else:
            return self.list(request)
        

class TopPostViewSet(generics.GenericAPIView, mixins.ListModelMixin):
    serializer_class = PostSerializer
    queryset = Post.objects.all().filter(publish_status=True)
    pagination_class = SetBlogPostPaginationResult
    filter_backends = [SearchFilter, OrderingFilter]

    def get_queryset(self):
        return Post.objects.filter(publish_status=True).annotate(
            hit_count=Count('hit_count_generic__hits')
        ).order_by('-hit_count', '-publish_date')[:6]

    def get(self, request):
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
        