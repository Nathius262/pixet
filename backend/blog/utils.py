from django.conf import settings
import os

def upload_location(instance, filename):
    file_path = 'blog/user_{author_id}/{slug}_post.jpeg'.format(
        author_id=str(instance.author.id), slug=str(instance.slug), filename=filename
    )
    full_path = os.path.join(settings.MEDIA_ROOT, file_path)
    if os.path.exists(full_path):
        os.remove(full_path)
    return file_path
