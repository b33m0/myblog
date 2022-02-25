from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_img = models.ImageField(upload_to='profile_img/%Y%m%d/', null=False, blank=True)
    profile_info = models.TextField(max_length=500, null=False, blank=True)

    def __str__(self):
        return 'user {}'.format(self.user.username)

