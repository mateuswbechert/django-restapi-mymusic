from django.contrib import admin
from django.apps import apps
from .models import Music, Album, Band, Member

admin.site.register(Band)
admin.site.register(Album)
admin.site.register(Music)
admin.site.register(Member)