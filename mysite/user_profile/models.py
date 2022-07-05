
from django.contrib.auth import get_user_model
from django.db import models
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(
        get_user_model(),
        on_delete=models.CASCADE,
        verbose_name='vartotojas',
        related_name='profile',
    )
    picture = models.ImageField(
        'nuotrauka',
        default='user/profile/default.png',
        upload_to='user/profile/pictures',
    )

    def __str__(self):
        return '{} profile'.format(str(self.user))

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        picture = Image.open(self.picture.path)
        if picture.height > 150 or picture.width > 150:
            output_size = (150, 150)
            picture.thumbnail(output_size)
            picture.save(self.picture.path)
