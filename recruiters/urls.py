from django.urls import path

from recruiters.views import create_job, job_description

urlpatterns = [
    path('jobs/<slug>', job_description, name='job-description'),
    path('new-job/', create_job, name='create-job')
]
