from django import forms
from candidates.models import Resume

class CreateResumeForm(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        super(CreateResumeForm, self).__init__(*args, **kwargs)
        self.fields['image'].widget.attrs.update(
            {
                'class':'custom-file-input',
                'id':'customFile',
                'type':'file'
            },
        ),
        self.fields['name'].widget.attrs.update(
            {
                'class':'form-control rounded',
                'placeholder':'Full Name',
                'type':'text'
            },
        ),
        self.fields['title'].widget.attrs.update(
            {
                'class':'form-control rounded',
                'type':'text',
                'placeholder':'Web Designer'
            },
        ),
        self.fields['category'].widget.attrs.update(
            {
                'class':'form-control rounded',
                'type':'text',
            },
        ),
        self.fields['email'].widget.attrs.update(
            {
                'class':'form-control rounded',
                'type':'email',
                'placeholder':'opper@gmail.com'
            },
        ),
        self.fields['content'].widget.attrs.update(
            {
                'class':'form-control rounded',
                'type':'text',
                'placeholder':'Resume Content'
            },
        ),
        self.fields['school_name'].widget.attrs.update(
            {
                'class':'form-control rounded',
                'type':'text',
                'placeholder':'School name here...'
            },
        ),


    class Meta:
        model = Resume
        fields = '__all__'
        # fields = ['name', 'image', 'title', 'category', 'email', 'content']