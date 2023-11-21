from django.contrib import admin
from .models import News
from .models import Rest
from .models import Comment
from .models import ContactMessage
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from .resources import NewsResource
from .resources import RestResource

class NewsResource(resources.ModelResource):
    class Meta:
        model = News
    def dehydrate_created_date(self, news):
        if news.created_date:
            return news.created_date.strftime("%Y-%m-%d %H:%M:%S")
        else:
            return "Нет даты"
    def dehydrate_title(self, news):
        return news.title.upper() if news.title else ""
class NewsAdmin(ImportExportModelAdmin):
    resource_class = NewsResource
    def get_export_queryset(self, request):
        queryset = super().get_export_queryset(request)
        return queryset.exclude(published_date__isnull=True)

    list_display = ('id', 'author', 'image', 'title', 'text', 'created_date', 'published_date')
    list_filter = ['author', 'created_date']
    date_hierarchy = 'created_date'
    def history_view(self, request, object_id, extra_context=None):
        extra_context = extra_context or {}
        extra_context['history_entries'] = News.objects.get(pk=object_id).history.all()
        return super().history_view(request, object_id, extra_context=extra_context)

admin.site.register(News, NewsAdmin)

class RestAdmin(ImportExportModelAdmin):
    resource_class = RestResource
    list_display = ('id', 'author', 'title', 'text')

    def history_view(self, request, object_id, extra_context=None):
        extra_context = extra_context or {}
        extra_context['history_entries'] = Rest.objects.get(pk=object_id).history.all()
        return super().history_view(request, object_id, extra_context=extra_context)

admin.site.register(Rest, RestAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'post', 'content', 'created_at')
    list_filter = ['author', 'created_at', 'post']
    date_hierarchy = 'created_at'

admin.site.register(Comment, CommentAdmin)

class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'message')
admin.site.register(ContactMessage, ContactMessageAdmin)