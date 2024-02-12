from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from .models import Profile

@receiver(user_logged_in)
def create_profile(sender, request, user, **kwargs):
    try:
        user_profile = user.profile
    except Profile.DoesNotExist:
        user_profile = Profile(user=user)
        user_profile.save()

        