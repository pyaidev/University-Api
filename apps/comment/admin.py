from django.contrib import admin
from django.forms import Textarea

from .models import *


# Register your models here.


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0
    fields = ('author', 'message')
    formfield_overrides = {
        models.TextField: {'widget': Textarea(
            attrs={'rows': 3,
                   'cols': 50})},
    }


class CommentAdmin(admin.ModelAdmin):
    inlines = [CommentInline]
    list_display = ('id', 'author', 'post_id', 'parent_id', 'top_level_comment_id', 'is_reply')
    search_fields = ['author__username']
    search_help_text = 'search on here'


admin.site.register(Comment, CommentAdmin)
