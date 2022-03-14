from django.contrib import admin
from .models import Recipe,comments

admin.site.register(Recipe)

admin.site.register(comments)