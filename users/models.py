from django.db import models
from django.contrib.auth.models import AbstractUser, User
from PIL import Image
from phonenumber_field.modelfields import PhoneNumberField
from .storage import OverwriteStorage
import os


# class CustomUser(AbstractUser):
#     def __str__(self):
#         return self.email


def get_upload_path(instance, filename):
    path = "profile_images/"
    ext = os.path.splitext(filename)[1].lower()
    path_format = str("user_%d" % instance.User.id) + "_%s" % instance.User.username + ext
    return os.path.join(path, path_format)


class Profile(models.Model):
    User = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='User')
    PhoneNumber = PhoneNumberField(blank=True, region='RU', verbose_name='Phone number')

    # PhoneNumber = PhoneNumberField(null=False, blank=True, unique=True, region='RU')

    class Meta:
        # verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def __str__(self):
        return f'{self.User.username}'


class ImageProfile(models.Model):
    User = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='User')
    image = models.ImageField(default='default.jpg', storage=OverwriteStorage(), upload_to=get_upload_path)

    def __str__(self):
        return f'{self.User.username}'

    def save(self, *args, **kwargs):
        super(ImageProfile, self).save(*args, **kwargs)
        img = Image.open(self.image.path)
        im_new = crop_max_square(img)
        im_new.save(self.image.path)


def crop_center(pil_img, crop_width, crop_height):
    img_width, img_height = pil_img.size
    return pil_img.crop(((img_width - crop_width) // 2,
                         (img_height - crop_height) // 2,
                         (img_width + crop_width) // 2,
                         (img_height + crop_height) // 2))


def crop_max_square(pil_img):
    return crop_center(pil_img, min(pil_img.size), min(pil_img.size))
