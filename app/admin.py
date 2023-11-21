from django.contrib import admin
from app.models import JobPost, Location, Author, Skills
class JobAdmin(admin.ModelAdmin):
    list_display = ('__str__','title','salary','date')
    list_filter = ('date','salary','expiry')
    search_fields = ('title',)
    search_help_text = "What are you looking for ?"

    fieldsets = (
        ('Basic informations:',{
            'fields':('title','description'),
        }),('More informations:',{
        'classes':('collapse',),
            'fields':(('expiry','salary'),'slug'),
        })
    )
# Register your models here.
admin.site.register(JobPost)
admin.site.register(Location)
admin.site.register(Author)
admin.site.register(Skills)