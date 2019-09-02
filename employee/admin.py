from django.contrib import admin
from .models import  Profile
from .models import Skill
from .models import Experience

# Register your models here.
admin.site.register(Profile)
admin.site.register(Skill)
admin.site.register(Experience)