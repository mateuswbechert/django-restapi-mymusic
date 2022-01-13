from django.contrib import admin
from django.db.models import fields
from .models import Music, Album, Band, Member

class MemberInline(admin.TabularInline):
    model = Member
    extra = 3

class BandAdmin(admin.ModelAdmin):
    inlines = [MemberInline]

admin.site.register(Band, BandAdmin)
admin.site.register(Album)
admin.site.register(Music)
admin.site.register(Member)