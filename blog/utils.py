from django.conf import settings
import uuid
import os


def upload_location(instance, filename):
    # Generate the file path based on the instance's author ID and slug
    file_path = 'blog/user_{author_id}/{slug}_post.jpeg'.format(
        author_id=str(instance.author.id), slug=str(instance.slug)
    )
    # Get the full path to the file
    full_path = os.path.join(settings.MEDIA_ROOT, file_path)
    # If the file already exists, remove it
    if os.path.exists(full_path):
        os.remove(full_path)
    return file_path

def generate_ref_code():
    code = str(uuid.uuid4())[:12]
    return code