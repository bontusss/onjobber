from django.db import models

# Create your models here.
class APIJOBS(models.Model):
    title = models.CharField(max_length=200, null=True)
    company_name = models.CharField(max_length=100, null=True, blank=True)
    slug = models.SlugField(null=True)
    description = models.TextField()
    url = models.URLField(null=True)
    location = models.CharField(max_length=100, null=True)
    job_type = models.CharField(max_length=50, null=True)
    job_level = models.CharField(max_length=100, null=True)
    created = models.DateTimeField(null=True)
    
    def __str__(self):
        return self.title
    
    
class Review(models.Model):
    name = models.CharField(max_length=100, null=True, help_text='Name of the reviewer')
    title = models.CharField(max_length=50, help_text='Eg. Product Manager', null=True)
    review = models.TextField(null=True)
    
    def __str__(self):
        return 'Review by' + ' ' + self.name
    
    
# email subscription
class Newsletter(models.Model):
    email = models.EmailField(null=True)
    
    def __str__(self):
        return self.email