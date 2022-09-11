from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()  # initiate django user model


class Profile(models.Model):
    """User profile. Include: id, bio, profile image, location."""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    bio = models.TextField(blank=True)
    profileimg = models.ImageField(upload_to='profile_images', default='blank-profile-picture')
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username
