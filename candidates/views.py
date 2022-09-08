from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

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
