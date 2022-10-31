from django.urls import path
from . import views


app_name = "candidates"
urlpatterns = [
    # path('<slug>/', views.candidate_detail, name="candidate-detail"),
    path('dashboard/', views.dashboard, name='candidate-dashboard'),
    path('create-resume/', views.create_resume, name="create-resume")
]
