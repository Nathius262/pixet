# Generated by Django 4.2.7 on 2023-12-13 03:23

import blog.utils
import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Tag",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, null=True)),
                ("date_created", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="Post",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=300, null=True)),
                ("body", ckeditor_uploader.fields.RichTextUploadingField()),
                (
                    "image",
                    models.ImageField(
                        blank=True, null=True, upload_to=blog.utils.upload_location
                    ),
                ),
                ("publish_status", models.BooleanField(default=False)),
                (
                    "publish_date",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="date published"
                    ),
                ),
                (
                    "date_updated",
                    models.DateTimeField(auto_now=True, verbose_name="date updated"),
                ),
                ("slug", models.SlugField(blank=True, unique=True)),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="author",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "tag",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="blog.tag",
                    ),
                ),
            ],
            options={
                "ordering": ("-publish_date", "-date_updated", "title", "author"),
            },
        ),
    ]
