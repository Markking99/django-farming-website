from django.contrib import admin
from django.contrib.admin.decorators import register

# Register your models here.
from .models  import Farmer, Member

admin.site.register (Farmer)
admin.site.register(Member)

