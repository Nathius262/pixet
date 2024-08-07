from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from django.conf import settings
from django.urls import reverse
from .utils import upload_location
from hitcount.models import HitCount
from django.contrib.contenttypes.fields import GenericRelation
from django.core.exceptions import ValidationError
from django.utils.text import slugify


# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=255, blank=False, null=True)
    date_created = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = (
            '-date_created',
            '-name'
        )

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=500, blank=False, null=True)
    tag = models.ManyToManyField(Tag, blank=False)
    body = CKEditor5Field(config_name='extends', null=False, blank=True)
    image = models.ImageField(upload_to=upload_location, null=True, blank=True)
    publish_status = models.BooleanField(default=False)
    publish_date = models.DateTimeField(auto_now_add=True, verbose_name="date published")
    date_updated = models.DateTimeField(auto_now=True, verbose_name="date updated")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="author")
    slug = models.SlugField(max_length=500, blank=True, unique=True)
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk',
                                    related_query_name='hit_count_generic_relation')

    @property
    def image_url(self):
        try:
            image = self.image.url
        except :
            image =""
        return image

    def get_absolute_url(self):
        return reverse('blog:detail_post_api', args=[self.slug])

    class Meta:
        ordering = (
            '-publish_date',
            "-date_updated",
            "title",
            "author",
        )

    def __str__(self):
        return self.title

    def clean(self):
        if not self.slug:
            self.slug = slugify(self.title)

        # Check if the slug is unique, if not, suggest a new unique slug
        original_slug = self.slug
        unique_slug = original_slug
        num = 1
        while Post.objects.exclude(pk=self.pk).filter(slug=unique_slug).exists():
            unique_slug = f"{original_slug}-{num:02d}"
            num += 1

        if unique_slug != original_slug:
            raise ValidationError({'slug': f"Slug '{original_slug}' is already in use. Suggested slug: '{unique_slug}'"})

        self.slug = unique_slug

    def save(self, *args, **kwargs):
        self.clean()  # Ensure the clean method is called
        super(Post, self).save(*args, **kwargs)


class NewsLetter(models.Model):
    email = models.EmailField(unique=True, blank=False, null=True)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.email)