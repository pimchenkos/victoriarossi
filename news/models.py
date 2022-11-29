from django.db import models
from django.utils import timezone
from users.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse
from .storage import OverwriteStorage
from PIL import Image
import os


def get_upload_path(instance, filename):
    path = "news_images/"
    ext = os.path.splitext(filename)[1].lower()
    format = str("article_%s" % instance.date) + "_%s" % instance.author.username + ext
    return os.path.join(path, format)


class Article(models.Model):
    title = models.CharField(max_length=200)
    text = RichTextUploadingField()
    date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(default='news-default.jpg', storage=OverwriteStorage(), upload_to=get_upload_path)

    # def __str__(self):
    #     return self.title

    def get_absolute_url(self):
        return reverse('news-detail', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        super(Article, self).save(*args, **kwargs)
        img = Image.open(self.image.path)
        img.save(self.image.path)
