from django.urls import path, include
from .views import index_view, ckeditor5_upload

urlpatterns = [
    path("api/", include("blog.api.urls")),
    path('', index_view, name='index'),
    path("upload", ckeditor5_upload, name="custom_upload_file"),
]
