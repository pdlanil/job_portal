from django.contrib import admin
from .models import Company_Profile
from .models import Job

# Register your models here.
admin.site.register(Company_Profile)
admin.site.register(Job)