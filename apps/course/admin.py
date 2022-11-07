from django.contrib import admin
from .models import Course, Lesson



class LessonInlineAdmin(admin.StackedInline):
    model = Lesson
    extra = 0


class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInlineAdmin]
    list_display = ('id', 'title', 'category', 'author')
    list_filter = ('id', 'category')
    search_fields = ['title', 'author__username']
    list_display_links = ('title', 'id',)
    list_per_page = 50
    date_hierarchy = 'created_at'
    search_help_text = 'search on here'



class LessonAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'course', 'duration', 'created_at')
    list_filter = ('course', )
    search_fields = ('title', 'course__title', 'duration')
    date_hierarchy = 'created_at'


admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
