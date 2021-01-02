from django.contrib import admin
from polls.models import Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question']}),
        ('Date Info', {'fields': ['published_date'], 'classes':['collapse']})
    ]
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)

