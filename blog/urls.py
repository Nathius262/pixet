from django.urls import path, include
from .views import index_view

urlpatterns = [
    path("api/", include("blog.api.urls")),
    path('', index_view, name='index'),
]
