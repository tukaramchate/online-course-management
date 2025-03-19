from django.contrib import admin
from .models import Courses

class CoursesAdmin(admin.ModelAdmin):
    list_display = ['id', 'course', 'is_active', 'created_at', 'updated_at']
    list_display_links = ['id', 'course', 'is_active', 'created_at', 'updated_at']
    search_fields = [ 'id']
    list_per_page = 20

admin.site.register(Courses,CoursesAdmin)
