from django.dispatch import receiver
from django.db.models.signals import pre_save, post_delete, post_save
from .models import Post
from PIL import Image
from django.utils.text import slugify

@receiver(post_delete, sender=Post)
def submission_delete(sender, instance, **kwargs):
    instance.image.delete(False)


@receiver(post_save, sender=Post)
def save_img(sender, instance, *args, **kwargs):
    SIZE = 600, 600
    if instance.image:
        pic = Image.open(instance.image.path)
        try:
            pic.thumbnail(SIZE, Image.LANCZOS)
            pic.save(instance.image.path)
        except:
            if pic.mode in ("RGBA", 'P'):
                blog_pic = pic.convert("RGB")
                blog_pic.thumbnail(SIZE, Image.LANCZOS)
                blog_pic.save(instance.image.path)        


def pre_save_blog_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.author.username + "-" + instance.title)


pre_save.connect(pre_save_blog_post_receiver, sender=Post)