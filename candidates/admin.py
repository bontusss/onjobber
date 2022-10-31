from django.contrib import admin

from candidates.models import Experience, Education, SavedJobs, Resume, AppliedJobs

# Register your models here.
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(SavedJobs)
admin.site.register(Resume)
admin.site.register(AppliedJobs)