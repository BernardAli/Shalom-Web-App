from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from PIL import Image
from core.models import Family, Auxiliaries

# Create your models here.


MARRIAGE_STATUS_CHOICE = (
    ('Single', 'Single'),
    ('Married', 'Married'),
    ('Divorced', 'Divorced'),
    ('Widowed', 'Widowed'),
)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField(null=True, blank=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics', null=True, blank=True)
    created = models.DateField(auto_now_add=True)
    marriage_status = models.CharField(max_length=20, choices=MARRIAGE_STATUS_CHOICE, default='User')
    phone = models.CharField(max_length=20)
    next_of_kin = models.CharField(max_length=100)
    next_of_kin_contact = models.CharField(max_length=100, null=True, blank=True)
    family = models.ForeignKey(Family, on_delete=models.DO_NOTHING, null=True, blank=True, default=1)
    auxiliaries = models.ForeignKey(Auxiliaries, on_delete=models.DO_NOTHING, null=True, blank=True, default=1)

    def get_absolute_url(self):
        return reverse('profile', args=[str(self.id)])

    def __str__(self):
        return str(self.user.username)

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
