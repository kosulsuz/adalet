from django.contrib import admin

from .models import Setting

class SettingAdmin(admin.ModelAdmin):
		
	list_display = ['title', 'icon', 'youtube_url','header', 'content', 'description']



admin.site.register(Setting, SettingAdmin)


