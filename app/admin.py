from django.contrib import admin
from app.models import JobPost
class JobAdmin(admin.ModelAdmin):
    list_display = ('__str__','title','salary','date')
    list_filter = ('date','salary','expiry')
    search_fields = ('title',)
    search_help_text = "What are you looking for ?"
# Register your models here.
admin.site.register(JobPost, JobAdmin)