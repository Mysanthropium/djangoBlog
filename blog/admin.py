from django.contrib import admin
from .models import Post, Comment, UserProfile
from django_summernote.admin import SummernoteModelAdmin

# Admin panel page

admin.site.register(UserProfile)
admin.site.register(Comment)

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on')
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    summernote_fields = ('content')
