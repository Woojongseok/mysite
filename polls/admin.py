from django.contrib import admin

from .models import Question, Choice


# class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    # fields = ['pub_date', 'question_text']
    fieldsets=[
        (None, {'fields': ['question_text']}),
        # ('Question', {'fields': ['question_text']}),
        ('Date information', {'fields':['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]

    # list_display = ['question_text','pub_date']
    list_display = ('question_text', 'pub_date', 'was_published_recently')

    list_filter = ['pub_date']          # Filter 기능 활성화(전체, 지난, 올해, 이번달 등등)
    search_fields = ['question_text']   # 검색 활성화
    

# admin.site.register(Question)
admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice)