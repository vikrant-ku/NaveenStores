from django.contrib import admin
from .models import Blog

# Register your models here.
class Blog_Admin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'date')
    search_fields = ('title', 'slug', 'status')
    prepopulated_fields = {'slug':('title',)}
    list_editable = ('status','date')
    list_filter = ('status', 'date')

admin.site.register(Blog, Blog_Admin)
