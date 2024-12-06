from django.db import models
from ckeditor.fields import RichTextField


class Post(models.Model):
    image = models.ImageField(upload_to='posts_image/')
    category = models.CharField(max_length=221)
    title = models.CharField(max_length=221)
    description = RichTextField()
    description2 = RichTextField()
    author_image = models.ImageField(upload_to='author_image/')
    author_name = models.CharField(max_length=221)
    author_job = models.CharField(max_length=221)
    post_add_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author_name


class SendEmail(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email

