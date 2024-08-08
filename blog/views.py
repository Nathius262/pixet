from django.shortcuts import render, redirect
from django.http import JsonResponse
import os
from decouple import config

import cloudinary
import cloudinary.uploader
from cloudinary.utils import cloudinary_url

# Configuration       
cloudinary.config(
    cloud_name=config('CLOUD_NAME'),
    api_key=config('API_KEY'),
    api_secret=config('API_SECRET'),
    secure=True,
    #api_proxy = "http://proxy.server:3128"
)


def ckeditor5_upload(request):
    if request.method == "POST":

        print(request.FILES)
        uploaded_file = request.FILES['upload']
        
        # Upload an image
        upload_result = cloudinary.uploader.upload(uploaded_file, folder="ckeditor_upload/")
        url = upload_result["secure_url"]
        print(url)
        
        return JsonResponse({
            "url": url,
        })
        


def index_view(request):
    return redirect('/admin/')