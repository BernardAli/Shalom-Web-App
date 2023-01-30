from PIL import Image
from django.db import models
from django.urls import reverse


class Subscribers(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email


class Services(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics', null=True, blank=True)
    times = models.CharField(max_length=255, blank=True, null=True)
    days = models.CharField(max_length=255, blank=True, null=True)
    descriptions = models.TextField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse('service_details', args=[str(self.id)])

    def __str__(self):
        return self.name


class Sermon(models.Model):
    service = models.ForeignKey(Services, on_delete=models.DO_NOTHING)
    date = models.DateField()
    preacher = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    file = models.FileField()

    def __str__(self):
        return self.title


class FAQ(models.Model):
    question = models.CharField(max_length=250)
    answer = models.TextField()

    def __str__(self):
        return self.question


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
    contact = models.CharField(max_length=13, blank=True, null=True)
    vision = models.TextField(blank=True, null=True)
    mission = models.TextField(blank=True, null=True)
    speech = models.TextField(blank=True, null=True)
    deacon = models.ImageField(default='group.png', upload_to='auxiliaries', blank=True, null=True)
    group_img = models.ImageField(default='group.png', upload_to='auxiliaries', blank=True, null=True)
    contribution_target = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('family_details', args=[str(self.id)])

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
    vision = models.TextField(blank=True, null=True)
    mission = models.TextField(blank=True, null=True)
    speech = models.TextField(blank=True, null=True)
    deacon = models.ImageField(default='group.png', upload_to='auxiliaries', blank=True, null=True)
    group_img = models.ImageField(default='group.png', upload_to='auxiliaries', blank=True, null=True)
    contribution_target = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('aux_details', args=[str(self.id)])

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super(Auxiliaries, self).save(*args, **kwargs)

        img = Image.open(self.group_img.path)

        if img.height > 600 or img.width > 500:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.group_img.path)


class AuxiliaryMeetings(models.Model):
    days = models.CharField(max_length=50, blank=True, null=True)
    time = models.CharField(max_length=50, blank=True, null=True)
    auxiliary = models.ForeignKey(Auxiliaries, on_delete=models.DO_NOTHING, related_name='auxiliary_meeting')

    def __str__(self):
        return self.auxiliary.name


class AuxiliaryExecutives(models.Model):
    auxiliary = models.ForeignKey(Auxiliaries, on_delete=models.DO_NOTHING, related_name='auxiliary_executives')
    full_name = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics', null=True, blank=True)
    phone_no = models.CharField(max_length=20, null=True, blank=True)
    facebook = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.auxiliary.name

    def save(self, *args, **kwargs):
        super(AuxiliaryExecutives, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 600 or img.width > 500:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class AuxiliariesFAQ(models.Model):
    auxiliary = models.ForeignKey(Auxiliaries, on_delete=models.DO_NOTHING, related_name='auxiliary_faqs')
    question = models.CharField(max_length=250)
    answer = models.TextField()

    def __str__(self):
        return self.question


class FamilyFAQ(models.Model):
    family = models.ForeignKey(Auxiliaries, on_delete=models.DO_NOTHING, related_name='family_faqs')
    question = models.CharField(max_length=250)
    answer = models.TextField()

    def __str__(self):
        return self.question


class Ministries(models.Model):
    name = models.CharField(max_length=255)
    goal = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    speech = models.TextField(blank=True, null=True)
    image = models.ImageField(default='group.png', upload_to='ministries')

    def get_absolute_url(self):
        return reverse('min_details', args=[str(self.id)])

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super(Ministries, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 600 or img.width > 500:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class UpcomingEvents(models.Model):
    event = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.event