from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from PIL import Image
from core.models import Family, Auxiliaries, Ministries

# Create your models here.


MARRIAGE_STATUS_CHOICE = (
    ('Single', 'Single'),
    ('Married', 'Married'),
    ('Divorced', 'Divorced'),
    ('Widowed', 'Widowed'),
)


WORK_STATUS_CHOICES = (
    ('Unemployed', 'Unemployed'),
    ('Employed', 'Employed'),
    ('Student', 'Student'),
)


EDUCATION_LEVEL_CHOICES = (
    ('No Formal Education', 'No Formal Education'),
    ('Junior High', 'Junior High'),
    ('Senior High', 'Senior High'),
    ('HND', 'HND'),
    ('Diploma', 'Diploma'),
    ('Degree', 'Degree'),
    ('Masters', 'Masters'),
    ('PHD', 'PHD'),
)

YES_NO_CHOICES = (
    ('Yes', 'Yes'),
    ('No', 'No'),
)

GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
)

BAPTISM_CHOICES = (
    ('Water', 'Water'),
    ('Holy Ghost', 'Holy Ghost'),
    ('Both', 'Both'),
    ('Not Yet', 'Not Yet'),
)

BLOOD_CHOICES = (
    ('O-', 'O-'),
    ('O+', 'O+'),
    ('A-', 'A-'),
    ('A+', 'A+'),
    ('AB-', 'AB-'),
    ('AB+', 'AB+'),
    ('B-', 'B'),
    ('B+', 'B+'),
)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    full_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=50, choices=GENDER_CHOICES, null=True, blank=True)
    blood_group = models.CharField(max_length=50, choices=BLOOD_CHOICES, null=True, blank=True)
    place_of_residence = models.CharField(max_length=50)
    birth_date = models.DateField(null=True, blank=True)
    work_status = models.CharField(max_length=50, choices=WORK_STATUS_CHOICES, default='Student')
    organisation_name = models.CharField(max_length=50, null=True, blank=True)
    education_level = models.CharField(max_length=50, choices=EDUCATION_LEVEL_CHOICES, null=True, blank=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics', null=True, blank=True)
    created = models.DateField(auto_now_add=True)
    hometown = models.CharField(max_length=50, null=True, blank=True)
    marital_status = models.CharField(max_length=20, choices=MARRIAGE_STATUS_CHOICE, default='Single')
    spouse = models.CharField(max_length=50, null=True, blank=True)
    no_of_children = models.IntegerField(null=True, blank=True)
    phone_no = models.CharField(max_length=20)
    email = models.CharField(max_length=50, null=True, blank=True)
    father_name = models.CharField(max_length=100, null=True, blank=True)
    father_alive = models.CharField(max_length=3, choices=YES_NO_CHOICES, default='Yes')
    mother_name = models.CharField(max_length=100, null=True, blank=True)
    mother_alive = models.CharField(max_length=3, choices=YES_NO_CHOICES, default='Yes')
    next_of_kin_contact = models.CharField(max_length=20, null=True, blank=True)
    date_joined = models.DateField(null=True, blank=True)
    baptism = models.CharField(max_length=10, choices=BAPTISM_CHOICES, default='Not Yet')
    family = models.ForeignKey(Family, on_delete=models.DO_NOTHING, null=True, blank=True, related_name='family')
    auxiliary = models.ForeignKey(Auxiliaries, on_delete=models.DO_NOTHING, null=True, blank=True)
    ministry = models.ForeignKey(Ministries, on_delete=models.DO_NOTHING, null=True, blank=True)
    is_deacon = models.BooleanField(default=False)
    is_council_member = models.BooleanField(default=False)

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