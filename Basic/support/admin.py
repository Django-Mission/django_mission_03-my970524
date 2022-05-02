from django.contrib import admin
from .models import Faq, Inquiry, Answer

# Register your models here.
class AnswerInline(admin.StackedInline):
    model = Answer
    extra = 5
    min_num = 3
    max_num = 5

@admin.register(Faq)
class FaqModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'updated_at')
    search_fields = ('title',)
    list_filter = ('category',)

@admin.register(Inquiry)
class InquiryModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at', 'writer')
    search_fields = ('title', 'email', 'phone_number')
    list_filter = ('category',)
    inlines = [AnswerInline]

    
