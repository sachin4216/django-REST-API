from django.contrib import admin
from myapp.models import Hero
# or --> from .models import Hero

admin.site.register(Hero)
