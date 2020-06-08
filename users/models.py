from django.db import models
from django.contrib.auth.models import User
from PIL import Image


TYPE_CHOICES = (
    ('Полный пакет', 'full'),
    ('Бесплатный пакет', 'free'),
)


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # on_delete что будет происходить, когда юзер будет удален. models.CASCADE - удалит информацию
    image = models.ImageField(default='default.png', upload_to='user_images')  # default - картинка оп умолчанию, upload_to - дирректория с картинками
    account_type = models.CharField(choices=TYPE_CHOICES, default='Бесплатный пакет', max_length=30)  # поле типа подписки аккаунта, по умолчанию - free

    def __str__(self):
        return f"Профиль пользователя {self.user.username}"

    def save(self, *args, **kwards):
        """изменение размера картинки"""
        super(Profile, self).save(*args, **kwards)
        img = Image.open(self.image.path)
        if img.height > 256 or img.width > 256:
            resize = (256, 256)
            img.thumbnail(resize)
            img.save(self.image.path)
