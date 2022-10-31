from django.contrib.auth.models import User
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.shortcuts import render, redirect
from users.forms import SignUpForm
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth import login
from django.http import HttpResponse
# from django.contrib import messages
from django.template.loader import render_to_string

from users.token import account_activation_token


# Create your views here.

def activation_sent(request):
    return render(request, 'registration/activation_sent.html')


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    #     check if the user exists and token is valid
    if user is not None and account_activation_token.check_token(user, token):
        #       if valid, set active true
        user.is_active = True
        #       set signup confirmation true
        user.profile.signup_confirmation = True
        user.save()
        login(request, user)
        return redirect('home')
    else:
        return render(request, 'registration/activation_invalid.html')


def sign_up(request):
    """
    Registers user and send email authentication email to the user.
    """
    if request.method == "POST":
        # check if cookies is enabled on the browser
        if request.session.text_cookie_worked():
            request.session.delete_test_cookie()
        else:
            # Refactor this code to show a better UI
            return HttpResponse("Please enable Cookies and try again.")
            
        request.session.set_test_cookie()
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.first_name = form.cleaned_data.get("first_name")
            user.profile.last_name = form.cleaned_data.get("last_name")
            user.profile.email = form.cleaned_data.get("email")
            user.profile.type = form.cleaned_data.get("account_type")
            # user.is_employer = form.cleaned_data.get("is_employer")
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            subject = 'Onjobber - Please Activate Your Account'
            # load template and call render method
            message = render_to_string('registration/activation_request.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)
            return redirect("activation_sent")

    else:
        form = SignUpForm()
    return render(request, "registration/register.html", {"form": form})
