from django import forms
from recruiters.models import Job,Skill


class NewJobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = "__all__"
        help_texts = {}
        excludes = ['recruiter']
        
    def __init__(self, *args, **kwargs):
        super(NewJobForm, self).__init__(*args, **kwargs)
        self.fields["title"].widget.attrs.update(
            {
                "placeholder": "Junior Web Developer",
                "class": "form-control rounded",
                "type": "text",
            }
        ),
        self.fields["description"].widget.attrs.update(
            {
                "placeholder": "Job Description",
                "class": "form-control rounded",
            }
        ),
        # self.fields["banner"].widget.attrs.update(
        #     {
        #         "placeholder": "",
        #         "class": "form-control rounded",
        #         'type': 'image'
        #     }
        # ),
        self.fields["location"].widget.attrs.update(
            {
                "placeholder": "Africa",
                "class": "form-control rounded",
                'type': 'text',
            }
        ),
        self.fields["skills"].widget.attrs.update(
            {
                "placeholder": "",
                "class": "form-control rounded",
            }
        ),
        self.fields["experience_level"].widget.attrs.update(
            {
                "placeholder": "",
                "class": "form-control rounded",
            }
        ),
        self.fields["type"].widget.attrs.update(
            {
                "placeholder": "",
                "class": "form-control rounded",
            }
        ),
        self.fields["deadline"].widget.attrs.update(
            {
                "placeholder": "yyyy-mm-dd",
                "class": "form-control rounded",
                'type': 'date'
            }
        ),
        self.fields["full_address"].widget.attrs.update(
            {
                "placeholder": "10 mark-john street, argon road.",
                "class": "form-control rounded",
                'type': 'text'
            }
        ),
        self.fields["country"].widget.attrs.update(
            {
                "placeholder": "Nigeria",
                "class": "form-control rounded",
                'type': 'text'
            }
        ),
        self.fields["state"].widget.attrs.update(
            {
                "placeholder": "Abia",
                "class": "form-control rounded",
                'type': 'text'
            }
        ),
        self.fields["company"].widget.attrs.update(
            {
                "placeholder": "Choose Company",
                "class": "form-control rounded",
            }
        ),
        self.fields["category"].widget.attrs.update(
            {
                "placeholder": "",
                "class": "form-control rounded",
            }
        ),
