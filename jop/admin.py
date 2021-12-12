from django.contrib import admin

# Register your models here.
from .models import jop,Category

admin.site.register(jop)

admin.site.register(Category)