from django import forms
from pages.models import Newsletter

class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super(NewsletterForm, self).__init__(*args, **kwargs)
        self.fields["email"].widget.attrs.update(
            {
                'placeholder': 'Enter Your Email Address', 
                'class': "form-control lg left-ico",
                'type': 'email'
            }
        )
        