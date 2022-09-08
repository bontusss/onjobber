from users.models import Profile


def get_profile_type(request):
    """
    context processor must return a dictionary.
    This method returns if the User.Profile.type is either "Employer" or "Candidate".
    """
    current_user = request.user
    pro = Profile.objects.filter(user=current_user).first()
    
    # other details
    site_name = 'OnJobber'
    site_description = 'Community for job seekers and employers.'
    return {
        'pro': pro,
        'site_name': site_name,
        'description': site_description,
    }
