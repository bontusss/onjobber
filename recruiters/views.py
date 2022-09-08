from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from recruiters.forms import NewJobForm
from django.contrib import messages

from recruiters.models import Job


def job_description(request, slug):
    job = get_object_or_404(Job, slug=slug)
    context = {'job': job}
    return render(request, "job-detail.html", context)


@login_required
def create_job(request):
    user = request.user
    if request.method == 'POST':
        form = NewJobForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Job saved')
            return redirect('home')
        else:
            messages.error(request, 'an error occurred')
    else:
        form = NewJobForm()
    context = {
        'form': form,
    }
    return render(request, 'post-job.html', context)