from django.contrib import admin

from .models import Card,Audio, Video
# Register your models here.

admin.site.register(Card)
admin.site.register(Audio)
admin.site.register(Video)