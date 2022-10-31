
from django.db import models

from recruiters.models import Job, Skill
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from autoslug import AutoSlugField
from django.utils import timezone
from ckeditor.fields import RichTextField


# A list of job types
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

CATEGORY = (
    ('Banking', 'Banking'),
    ('Medical', 'Medical'),
    ('Technology', 'Technology'),
)


    
    
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


class Education(models.Model):
    """
    Education history added to resume
    """
    school_name = models.CharField(max_length=100, help_text="The School you attended")
    degree_title = models.CharField(max_length=100, help_text="Eg. Masters in Computer Science")
    start_date = models.DateField()
    end_date = models.DateField()
    note = models.TextField(help_text="Brief info about this qualification.")

    def __str__(self):
        return '{} from {}'.format(self.degree_title, self.school_name)


class Experience(models.Model):
    employer = models.CharField(max_length=100, help_text="The name of the company you have worked for.")
    job_title = models.CharField(max_length=100, help_text="Your job title at the company.")
    start_date = models.DateField()
    end_date = models.DateField()
    note = models.TextField(help_text="Brief info about your work at the company.")

    def __str__(self):
        return '{} at {}'.format(self.job_title.title, self.employer.title)

class Resume(models.Model):
    image = models.ImageField(upload_to="resumes/image", blank=True)
    name = models.CharField(max_length=200, blank=True)
    title = models.CharField(max_length=100, blank=True, default="Eg: Web Developer")
    category = models.CharField(choices=CATEGORY, blank=True, max_length=100)
    email = models.EmailField(blank=True)
    content = models.TextField(blank=True)
    employer = models.CharField(max_length=100, help_text="The name of the company you have worked for.")
    job_title = models.CharField(max_length=100, help_text="Your job title at the company.")
    start_date = models.DateField()
    end_date = models.DateField()
    note = models.TextField(help_text="Brief info about your work at the company.")
    school_name = models.CharField(max_length=100, help_text="The School you attended")
    degree_title = models.CharField(max_length=100, help_text="Eg. Masters in Computer Science")
    start_date = models.DateField()
    end_date = models.DateField()
    note = models.TextField(help_text="Brief info about this qualification.")

    def __str__(self):
        return 'Resume for {}'.format(self.job_title)
