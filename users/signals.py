from django.contrib.auth.models import User
from .models import Profile, ImageProfile
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(User=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()


@receiver(post_save, sender=User)
def create_image_profile(sender, instance, created, **kwargs):
    if created:
        ImageProfile.objects.create(User=instance)


@receiver(post_save, sender=User)
def save_image_profile(sender, instance, **kwargs):
    instance.imageprofile.save()
