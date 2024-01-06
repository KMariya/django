from django.contrib import admin
from .models import Question, Choice
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'choice_text', 'votes')
    list_filter = ['question', 'choice_text', 'votes']

admin.site.register(Choice, ChoiceAdmin)


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'question_text', 'pub_date')
    list_filter = ['pub_date']
    date_hierarchy = 'pub_date'
    inlines = [ChoiceInline]
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)