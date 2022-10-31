from unicodedata import category
from django.shortcuts import render, redirect
# import requests
from django.contrib import messages
# from candidates.models import Profile
from pages.forms import NewsletterForm

from pages.models import APIJOBS, Review
from recruiters.models import Category, Job
from users.models import Profile


# Create your views here.
def index(request):
    # this throws an error when user is not authenticated
    current_user = request.user

    if request.user is not None:
        profile = Profile.objects.filter(user=current_user).first()

    categories = Category.objects.filter(is_active=True)
    jobs = Job.objects.all()
    # candidates = Profile.objects.filter(is_candidate=True)
    reviews = Review.objects.all()[::-3]
    popular_jobs = Job.objects.filter(popular=True)
    # email subscription
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have subscribed to our email list.')
            return redirect('home')
    else:

        form = NewsletterForm()
        # messages.error(request, 'Enter a valid email address')

    context = {
        "jobs": jobs,
        # "candidates": candidates,
        "reviews": reviews,
        'form': form,
        'popular_jobs': popular_jobs,
        'categories': categories,
        'profile': profile,
    }
    return render(request, "index.html", context)


# def get_api_jobs(request):
#     # all_api_jobs = {}
#     url = "https://www.arbeitnow.com/api/job-board-api"
#     response = requests.get(url)
#     data = response.json()
#     jobs = data["data"]
#
#     for j in jobs:
#         jobs_data = APIJOBS(
#             title=j["title"],
#             company_name=j["company_name"],
#             description=j["description"],
#         )
#
#     jobs_data.save()
#     all_api_jobs = APIJOBS.objects.all().order_by("-id")
#     return render(request, "index.html")
