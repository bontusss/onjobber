from django.contrib import admin

from recruiters.models import Award, Category, Company, Industry, Job, Skill

# Register your models here.
admin.site.register(Award)
admin.site.register(Skill)
admin.site.register(Company)
admin.site.register(Industry)
admin.site.register(Job)
admin.site.register(Category)