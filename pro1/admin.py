from django.contrib import admin
from .models import Recipe,comments,category

admin.site.register(Recipe)

admin.site.register(comments)
admin.site.register(category)
