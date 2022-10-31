from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404
from candidates.forms import CreateResumeForm

from users.models import Profile


# from candidates.models import Profile


# def candidate_detail(request, slug):
#     # candidate = get_object_or_404(Profile, slug=slug)
#     # context = {'candidate': candidate}
#     return render(request, 'candidate-detail.html')


@login_required
def dashboard(request):
    candidate = request.user
    profile = Profile.objects.filter(user=candidate).first()
    context = {
        'profile': profile,
    }
    return render(request, 'candidate/dashboard.html', context)



def create_resume(request):
    if request.method == 'POST':
        form = CreateResumeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Resume was created successfully!')
            return redirect('create-resume')
        else:
            messages.error(request, 'Resume was not created!')
    else:
        form = CreateResumeForm()
    return render(request, 'candidate/create-resume.html', {'form': form})