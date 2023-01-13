from PIL import Image
from django.db import models
from django.urls import reverse

# Create your models here.
MEMBER_CHOICE = (
    ('Already a Member', 'Already a Member'),
    ('New Member', 'New Member')
)


class InterestedMember(models.Model):
    full_name = models.CharField(max_length=250)
    contact = models.CharField(max_length=250)
    email = models.EmailField(blank=True, null=True)
    member_status = models.CharField(choices=MEMBER_CHOICE, max_length=20)

    def __str__(self):
        return self.full_name


MEMBER_CHOICES = (
    ('Reject', 'Reject'),
    ('Accept', 'Accept'),
)


class InterestedMemberAcceptance(models.Model):
    member = models.ForeignKey(InterestedMember, on_delete=models.CASCADE, related_name='interested_person')
    status = models.CharField(max_length=250, choices=MEMBER_CHOICES)

    def __str__(self):
        return str(self.member)


class Family(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(default='group.png', upload_to='blog_pics')
    contribution_target = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('Family', args=[str(self.id)])

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super(Family, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 600 or img.width > 500:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class Auxiliaries(models.Model):
    name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(default='group.png', upload_to='blog_pics')
    contribution_target = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('Auxiliaries', args=[str(self.id)])

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super(Auxiliaries, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 600 or img.width > 500:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)