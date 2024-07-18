from django.urls import path
from .views import PostViewSet,TagViewSet, TagFilterPostViewSet, TopPostViewSet

app_name = 'blog'

urlpatterns = [
    path('post/<slug>/', PostViewSet.as_view(), name='detail_post_api'),
    path('post/', PostViewSet.as_view(), name='list_post_api'),
    path('trends/', TopPostViewSet.as_view(), name='trend_post_api'),
    path('tag/', TagViewSet.as_view(), name='list_tag_api'),
    path('tag/<tag>', TagFilterPostViewSet.as_view(), name='filter_tag_api'),
]