from django.contrib import admin

from .models import Image


class ImageAdmin(admin.ModelAdmin):
	list_display = ['short_title', 'timeStamp']


admin.site.register(Image, ImageAdmin)


"""
	username: Admin
	password: scrape-it
"""
