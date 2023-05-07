from django.contrib import admin
from .models import News, Categories, Tags
# Register your models here.
admin.site.register(News)
admin.site.register(Categories)
admin.site.register(Tags)