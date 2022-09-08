from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

TYPE = (
    ('CANDIDATE', 'Candidate'),
    ('EMPLOYER', 'Employer'),
)


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'placeholder': 'Peter'}))
    last_name = forms.CharField(max_length=20)
    email = forms.EmailField(max_length=200)
    account_type = forms.ChoiceField(choices=TYPE)
    # is_employer = forms.BooleanField(help_text='Signup as an employer')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update(
            {
                'class': 'form-control',
                'type': 'text',
                'placeholder': 'Peter'
            }
        ),
        self.fields['last_name'].widget.attrs.update(
            {
                'class': 'form-control',
                'type': 'text',
                'placeholder': 'Obi'
            }
        ),
        self.fields['username'].widget.attrs.update(
            {
                'class': 'form-control',
                'type': 'text',
                'placeholder': 'obidient'
            }
        ),
        self.fields['email'].widget.attrs.update(
            {
                'class': 'form-control',
                'type': 'email',
                'placeholder': 'fake@email.com'
            }
        ),
        self.fields['account_type'].widget.attrs.update(
            {
                'class': 'form-control',
                'type': '',
                # 'placeholder': 'fake@email.com'
            }
        ),
        self.fields['password1'].widget.attrs.update(
            {
                'class': 'form-control',
                'type': '',
                # 'placeholder': 'fake@email.com'
            }
        ),
        self.fields['password2'].widget.attrs.update(
            {
                'class': 'form-control',
                'type': '',
                # 'placeholder': 'fake@email.com'
            }
        ),

    class Meta:
        model = User
        widgets = {}
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'account_type', ]
