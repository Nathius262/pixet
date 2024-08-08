from django.dispatch import receiver
from django.db.models.signals import pre_save, post_delete, post_save
from .models import Post, NewsLetter
from PIL import Image
import requests
from io import BytesIO
from django.conf import settings
from django.core.mail import send_mail
from .utils import truncate_html


@receiver(post_delete, sender=Post)
def submission_delete(sender, instance, **kwargs):
    instance.image.delete(False)

@receiver(post_save, sender=Post)
def save_img(sender, instance, *args, **kwargs):
    if not settings.DEBUG:
        SIZE = 600, 600
        if instance.image:

            image_url = instance.image.url

            # Download the image from the URL
            response = requests.get(image_url)

            # Open the image from the downloaded content
            pic = Image.open(BytesIO(response.content))
            try:
                pic.thumbnail(SIZE, Image.LANCZOS)
                pic.save(instance.image.path)
            except:
                if pic.mode in ("RGBA", 'P'):
                    blog_pic = pic.convert("RGB")
                    blog_pic.thumbnail(SIZE, Image.LANCZOS)
                    blog_pic.save(instance.image.path)


@receiver(post_save, sender=Post)
def send_newsletter_email(sender, instance, created, **kwargs):
    if created:
        subscribers = NewsLetter.objects.all()
        # Truncate the blog content
        truncated_content = truncate_html(instance.body, length=100)
        
        html_message = f"""
            <html>
                <body>
                    <p>Hello,</p>
                    <p>A new blog post has been published:</p>
                    <h2>{instance.title}</h2>
                    <img src="{instance.image_url}" alt="{instance.title}" style="max-width: 100%; height: auto;">
                    <p>{truncated_content}</p>
                    <p><a href="https://www.pixtinfinity.com/blog/{instance.slug}">Learn More</a></p>
                    <p>Thank you for subscribing to our newsletter!</p>
                </body>
            </html>
        """

        # Send an email to each subscriber
        for subscriber in subscribers:
            send_mail(
                subject=f"New Blog Post: {instance.title}",
                message=f"Hello,\n\nA new blog post has been published: \n{instance.title}\n\n{truncated_content}\n\nhttps://pixtinfinity.com/blog/{instance.slug}\n\nThank you for subscribing to our newsletter!",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[subscriber.email],
                fail_silently=False,
                html_message=html_message,
            )
"""
@receiver(post_save, sender=Post)
def save_img(sender, instance, created, *args, **kwargs):
    if created and instance.image:  # Check if a new instance is created and if it has an image
        file_path = instance.image_url
        try:

            # Perform transformation using Cloudinary
            transformed_image = cloudinary.CloudinaryImage(file_path).image(
                width=500, height=500, gravity="auto", crop="fill"
            )

            # Save the secure URL provided by Cloudinary to your instance
            instance.image = transformed_image
            instance.save()
        except Exception as e:
            print("Error:", e)
"""

"""@receiver(post_save, sender=Post)
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


@receiver(post_save, sender=Post)
def save_img(sender, instance, created, *args, **kwargs):
    if not created:
        SIZE = 600, 600
        if instance.image:

            import cloudinary.uploader
            file_path = instance.image.path
            pic = Image.open(file_path)
            try:
                pic.thumbnail(SIZE, Image.LANCZOS)
                cloudinary_response = cloudinary.uploader.upload(file_path)
                pic.save(cloudinary_response['secure_url'])
            except:
                if pic.mode in ("RGBA", 'P'):
                    profile_pic = pic.convert("RGB")
                    profile_pic.thumbnail(SIZE, Image.LANCZOS)
                    cloudinary_response = cloudinary.uploader.upload(file_path)
                    profile_pic.save(cloudinary_response['secure_url'])
 """

def pre_save_blog_post_receiver(sender, instance, *args, **kwargs):
    instance.clean()


pre_save.connect(pre_save_blog_post_receiver, sender=Post)