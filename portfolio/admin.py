from django.contrib import admin
from .models import Experience, Project, ContactMessage

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'start_date', 'end_date')
    search_fields = ('title', 'company')
    list_filter = ('company',)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'tech_stack', 'github_link', 'live_link')
    search_fields = ('title', 'tech_stack')
    list_filter = ('tech_stack',)

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    search_fields = ('name', 'email', 'message')
    list_filter = ('created_at',)
    readonly_fields = ('created_at',)