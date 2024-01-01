from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

# This function is called whenever a user is created
# It creates a profile for the user
# It is a receiver of the post_save signal
# It takes all the arguments of the post_save signal
# It also takes a created argument which is a boolean
# It is true if the user is created and false if the user is updated
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()