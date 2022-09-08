from django.db import models
from autoslug import AutoSlugField
from django.urls import reverse
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

JOB_TYPE = (
    ("Full Time", "Full Time"),
    ("Internship", "Internship"),
    ("Remote", "Remote"),
)

LEVEL = (
    ("Beginner", "Beginner"),
    ("Intermediate", "Intermediate"),
    ("Senior", "Senior"),
)


class Award(models.Model):
    title = models.CharField(max_length=100)
    year = models.DateTimeField()
    about = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title


class Skill(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    facebook = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    linkedin = models.URLField(null=True, blank=True)
    slug = AutoSlugField(populate_from='name', unique=True)
    phone_number = models.CharField(null=True, blank=True, max_length=15)
    about = models.TextField()
    award = models.ForeignKey(Award, on_delete=models.CASCADE)
    owner = models.ForeignKey(User ,related_name='companies', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return '/{}'.format(self.slug)


class Industry(models.Model):
    name = models.CharField(max_length=100, help_text="Eg. IT & Software")

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100, null=True)
    slug = AutoSlugField(populate_from='name', unique=True)
    icon = models.CharField(max_length=50, default='lni lni-laptop-phone')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # return reverse("model_detail", kwargs={"pk": self.pk})
        return '/categories/{}'.format(self.slug)


class Job(models.Model):
    title = models.CharField(max_length=200)
    # banner = models.ImageField(upload_to="job_banners")
    location = models.CharField(max_length=100)
    description = RichTextField()
    popular = models.BooleanField(default=False)
    slug = AutoSlugField(populate_from='title', unique=True)
    skills = models.ManyToManyField(Skill)
    experience_level = models.CharField(max_length=50, choices=LEVEL, default="Senior")
    type = models.CharField(max_length=50, choices=JOB_TYPE, default="Full Time")
    company = models.ForeignKey(Company, related_name='jobs', on_delete=models.CASCADE)
    deadline = models.DateField(null=True)
    full_address = models.CharField(max_length=255, null=True)
    country = models.CharField(max_length=100, null=True)
    state = models.CharField(max_length=100, null=True)
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('job-description', args=[self.slug])
