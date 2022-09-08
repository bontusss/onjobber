from django.db import models

from recruiters.models import Job, Skill
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from autoslug import AutoSlugField
from django.utils import timezone
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

SALARIES= (
    ("1", "10-20k"),
    ("2", "20-30k"),
    ("3", "30-40k"),
)

AGES= (
    ("1", "18-25 Years"),
    ("2", "26-35 Years"),
    ("3", "36-45 Years"),
    ("4", "46-55 Years"),
)


class Qualification(models.Model):
    title = models.CharField(max_length=200, help_text="Title of the qualification.")
    institution = models.CharField(
        max_length=100, help_text="Institution you got it from."
    )
    year = models.DateTimeField()
    about = models.TextField(help_text="Brief info about this qualification.")

    def __str__(self):
        return self.title


class Experience(models.Model):
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=50)
    job_title = models.CharField(max_length=100)
    started = models.DateTimeField()
    ended = models.DateTimeField()
    about = models.TextField()

    def __str__(self):
        return self.title


# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='profile')
#     full_name = models.CharField(max_length=100, null=True)
#     job_title = models.CharField(max_length=100, null=True, help_text='Javascript Developer')
#     bio = RichTextField()
#     slug = AutoSlugField(populate_from='user', unique=True)
#     phone = models.CharField(max_length=15, null=True)
#     skills = models.ManyToManyField(Skill)
#     email = models.CharField(max_length=100, null=True)
#     Country = CountryField(max_length=100, null=True, blank_label='(select country)')
#     resume = models.FileField(upload_to='resumes', null=True, blank=True)
#     job_type = models.CharField(max_length=50, choices=JOB_TYPE, default='Full Time')
#     experience_level = models.CharField(max_length=50, choices=LEVEL, default='Beginner', help_text='Eg: Beginner, '
#                                                                                                     'Senior')
#     current_salary = models.CharField(max_length=50, choices=SALARIES,default='1', help_text='10-50k')
#     language = models.CharField(max_length=100, null=True, help_text='Eg: English, Hindi')
#     location = models.CharField(max_length=255, null=True, blank=True)
#     age = models.CharField(max_length=50, choices=AGES, default='2')
#     qualifications = models.ManyToManyField(Qualification)
#     looking_for = models.CharField(max_length=50, choices=JOB_TYPE, default="Remote")
#     facebook_link = models.URLField(blank=True, null=True)
#     twitter_link = models.URLField(blank=True, null=True)
#     linkedin_link = models.URLField(blank=True, null=True)
#     github_link = models.URLField(blank=True, null=True)
    
#     def get_absolute_url(self):
#         return "/{}".format(self.slug)

#     def save(self, *args, **kwargs):
#         super().save(*args, **kwargs)

#     def __str__(self):
#         return self.user.username
    
    
class SavedJobs(models.Model):
    job = models.ForeignKey(
        Job, related_name='saved_job', on_delete=models.CASCADE)
    user = models.ForeignKey(
        User, related_name='saved', on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.job.title
    

class AppliedJobs(models.Model):
    job = models.ForeignKey(
        Job, related_name='applied_job', on_delete=models.CASCADE)
    user = models.ForeignKey(
        User, related_name='applied_user', on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.job.title