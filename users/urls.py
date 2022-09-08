from django.urls import path
from .views import sign_up, activation_sent, activate
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/', sign_up, name='signup'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LoginView.as_view(), name='logout'),
    path('sent/', activation_sent, name="activation_sent"),
    path('activate/<slug:uidb64>/<slug:token>', activate, name="activate")
]
