from django.contrib import admin
from MainApp.models import JobPost, Location, Author, Skills

class JobAdmin(admin.ModelAdmin):
    list_display = ("__str__", 'description', 'date', 'expiry')
    list_filter = ('date', 'expiry', 'salary')
    search_fields = ['title']
    search_help_text = 'write in your query and hit enter'
    # fields = (('title', 'description', 'salary'), 'expiry')
    # exclude = ('slug')
    fieldsets = (
        ('Basic information', {
            'fields' : ('title', 'description', 'salary')
        }),
        ('More information', {
            'classes': ('collapse',),
            'fields': ('expiry', 'slug')
        })
    )
# Register your models here.
admin.site.register(JobPost)
admin.site.register(Location)
admin.site.register(Author)
admin.site.register(Skills)