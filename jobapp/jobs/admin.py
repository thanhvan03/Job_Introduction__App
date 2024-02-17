from urllib import request

from django.contrib import admin
from django.template.response import TemplateResponse
from django.utils.safestring import mark_safe
from .models import Category, JobListing, Tag, User, JobApplication
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.urls import path
from jobs import dao

class JobAppAdminSite(admin.AdminSite):
    site_header = 'Job Placement System'

    def get_urls(self):
        return [
            path('job-stats/', self.stats_view)
        ] + super().get_urls()

    def stats_view(self, request):
        return TemplateResponse(request, 'admin/stats.html', {
            'stats': dao.count_applications_by_quarter_and_year()
            #'stats': dao.count_applications_by_year(),
            #'stats': dao.count_applications_by_quarter()
        })

class JobListingForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget)
    class Meta:
        model = JobListing
        fields = '__all__'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'created_date', 'updated_date', 'active']
    ordering = ['id']
    list_filter = ['id', 'name']
    search_fields = ['name']

class TagInlineAdmin(admin.StackedInline):
    model = JobListing.tags.through

class JobListingAdmin(admin.ModelAdmin):
    list_filter = ('category', 'tags')

    list_display = ['pk', 'title', 'created_date', 'updated_date', 'active']
    ordering = ['id']

    form = JobListingForm
    inlines = [TagInlineAdmin]


class UserAdmin(admin.ModelAdmin):
    readonly_fields = ['display_avatar']

    list_display = ['pk', 'username', 'role', 'date_joined', 'is_active']
    ordering = ['id']

    def display_avatar(self, user):
        if user.avatar:
            return mark_safe('<img src="/static/{url}" width="120" />'.format(url=user.avatar.name))
        return ''

    display_avatar.allow_tags = True
    display_avatar.short_description = 'Avatar'

class JobApplicationAdmin(admin.ModelAdmin):
    readonly_fields = ['cv']

    def name(self, obj):
        return f'{obj.job.title} - {obj.candidate.username}'

    list_display = ['pk', 'name', 'created_date', 'updated_date', 'active']
    ordering = ['id']

    def cv(self, jobapplication):
        if jobapplication.resume:
            return mark_safe('<img src="/static/{url}" width="120" />'.format(url=jobapplication.resume.name))
        return ''

class TagAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'created_date']
    ordering = ['id']



admin_site = JobAppAdminSite(name='jobapp')

admin_site.register(Category, CategoryAdmin)
admin_site.register(JobListing, JobListingAdmin)
admin_site.register(Tag, TagAdmin)
admin_site.register(User,UserAdmin)
admin_site.register(JobApplication,JobApplicationAdmin)