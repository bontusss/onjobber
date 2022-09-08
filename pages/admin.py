from django.contrib import admin

from pages.models import APIJOBS, Newsletter, Review

# Register your models here.
admin.site.register(APIJOBS)
admin.site.register(Review)
admin.site.register(Newsletter)