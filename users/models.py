from autoslug import AutoSlugField
from ckeditor.fields import RichTextField
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django_countries.fields import CountryField
# from phonenumber_field.modelfields import PhoneNumberField

USER_TYPE = (
    ('Candidate', 'Candidate'),
    ('Employer', 'Employer'),
)

LEVEL = (
    ('BEGINNER', 'Beginner'),
    ('INTERMEDIATE', 'Intermediate'),
    ('SENIOR', 'Senior'),
)


class Skill(models.Model):
    name = models.CharField(max_length=200)


class Certificate(models.Model):
    title = models.CharField(max_length=200, help_text='Title of the certificate')
    about = RichTextField(help_text='Brief info about the certificate')
    institution = models.CharField(max_length=200, help_text='Where did you get the certificate')
    year = models.DateField()

    def __str__(self):
        return self.title


class Profile(models.Model):
    first_name = models.CharField('first name', max_length=100)
    last_name = models.CharField('last name', max_length=100)
    email = models.EmailField(max_length=150)
    Profession = models.CharField(max_length=100, null=True, help_text='Javascript Developer', blank=True)
    bio = RichTextField(null=True, help_text='Tell employers about yourself', blank=True)
    slug = AutoSlugField(populate_from='user', unique=True, null=True)
    # phone = PhoneNumberField(blank=True)
    skills = models.ManyToManyField(Skill, blank=True)
    certificates = models.ManyToManyField(Certificate, blank=True)
    experience_level = models.CharField(max_length=20, choices=LEVEL, default='BEGINNER')
    Country = CountryField(max_length=100, null=True, blank_label='(select country)', blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=20, choices=USER_TYPE, default='Candidate')
    signup_confirmation = models.BooleanField(default=False)
    facebook = models.URLField(null=True, blank=True)
    github = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    instagram = models.URLField(null=True, blank=True)
    gitlab = models.URLField(null=True, blank=True)
    bitbucket = models.URLField(null=True, blank=True)
    behance = models.URLField(null=True, blank=True)
    portfolio = models.URLField(null=True, blank=True)

    def get_absolute_url(self):
        return '/profile/{}'.format()

    def __str__(self):
        return self.user.username

    def get_profile_type(self):
        return self.type


@receiver(post_save, sender=User)
def update_profile_signal(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
