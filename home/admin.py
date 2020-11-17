from django.contrib import admin

from .models import Setting, About, AboutLogo, Skill, Testimonials, Resume, Service, CompanyType, Reference, ContactInfo

class SettingAdmin(admin.ModelAdmin):
		
	list_display = ['title', 'icon', 'youtube_url','header', 'content', 'description']

class ContactInfoAdmin(admin.ModelAdmin):
		
	list_display = ['name', 'email', 'topic', "content"]

class ResumeAdmin(admin.ModelAdmin):
		
    list_display = ['sub_title', 'sub1_title',"ranking"]
    list_editable = ["ranking", ]


class AboutLogoInline(admin.TabularInline):
    model = AboutLogo

class SkillInline(admin.TabularInline):
    model = Skill

class TestimonialsInline(admin.TabularInline):
    model = Testimonials

class AboutAdmin(admin.ModelAdmin):
    inlines = [
        AboutLogoInline,
        SkillInline,
        TestimonialsInline,
    ]

class ReferenceInline(admin.TabularInline):
    model = Reference

class CompanyTypeAdmin(admin.ModelAdmin):
    inlines = [
        ReferenceInline,
    ]


admin.site.register(Setting, SettingAdmin)
admin.site.register(About, AboutAdmin)
admin.site.register(Resume, ResumeAdmin)
admin.site.register(CompanyType, CompanyTypeAdmin)
admin.site.register(ContactInfo, ContactInfoAdmin)
admin.site.register(Service)


