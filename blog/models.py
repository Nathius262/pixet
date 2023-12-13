from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.conf import settings
from django.urls import reverse
from .utils import upload_location

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=255, blank=False, null=True)
    date_created = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    
class Post(models.Model):
    title = models.CharField(max_length=300, blank=False, null=True)
    tag = models.ForeignKey(Tag, on_delete=models.SET_NULL, null=True, blank=False)
    body = RichTextUploadingField(null=False, blank=False)
    image = models.ImageField(upload_to=upload_location, null=True, blank=True)
    publish_status = models.BooleanField(default=False)
    publish_date = models.DateTimeField(auto_now_add=True, verbose_name="date published")
    date_updated = models.DateTimeField(auto_now=True, verbose_name="date updated")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="author")
    slug = models.SlugField(blank=True, unique=True)
    
    @property
    def image_url(self):
        try:
            image = self.image.url
        except :
            image =""
        return image
    

    """def get_absolute_url(self):
        return reverse('blog:details', args=[self.slug])"""

    class Meta:
        ordering = (
            '-publish_date',
            "-date_updated",
            "title",
            "author",
        )

    def __str__(self):
        return self.title
