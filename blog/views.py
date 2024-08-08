from django.shortcuts import render, redirect
from django.http import JsonResponse
from cloudinary.uploader import upload
from cloudinary.utils import cloudinary_url
from cloudinary.uploader import upload_image
import os

def ckeditor5_upload(request):
    if request.method == "POST":
        # Bypass the proxy for the Cloudinary API
        os.environ['NO_PROXY'] = 'api.cloudinary.com'

        print(request.FILES)
        uploaded_file = request.FILES['upload']
        
        # Upload the file directly to Cloudinary
        upload_result = upload_image(
            uploaded_file,
            folder="blog_images/",  # Your desired folder path
        )
        
        # Generate the URL for the uploaded image
        url, options = cloudinary_url(upload_result['public_id'], format="jpg")
        
        return JsonResponse({
            "url": url,
        })
# Create your views here.
def index_view(request):
    return redirect('/admin/')