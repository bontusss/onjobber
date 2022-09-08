from django import template

from users.models import Profile

register = template.Library()


@register.tag
def get_profile_type(request):
    current_user = request.user
    profile = Profile.objects.filter(user=current_user).first()
    if profile.type == 'Employer':
        return 'Employer'
    else:
        return 'Candidate'
