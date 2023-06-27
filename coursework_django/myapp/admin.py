
from django.contrib import admin
from .models import News
from .models import Rest
from .models import Comment
from .models import ContactMessage

class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'image', 'title', 'text', 'created_date', 'published_date')
    list_filter = ['author', 'created_date']
    date_hierarchy = 'created_date'

admin.site.register(News, NewsAdmin)

class RestAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'title', 'text')

admin.site.register(Rest, RestAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'post', 'content', 'created_at')
    list_filter = ['author', 'created_at', 'post']
    date_hierarchy = 'created_at'

admin.site.register(Comment, CommentAdmin)


class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'message')
admin.site.register(ContactMessage, ContactMessageAdmin)