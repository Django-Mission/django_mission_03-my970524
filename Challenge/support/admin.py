from django.contrib import admin, messages
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
    list_display = ('title', 'category', 'created_at', 'writer', 'status')
    search_fields = ('title', 'email', 'phone_number', 'writer__username')
    list_filter = ('category', 'status')
    inlines = [AnswerInline]
    def send_inquiry_closed_message(self, request, queryset):
        for obj in queryset:
            if (obj.is_email == True) and (obj.is_phone == True):
                self.message_user(request,'답변 완료 안내문을 발송하였습니다.')
                print(f'{obj.writer}의 이메일: {obj.email}')
                print(f'{obj.writer}의 전화번호: {obj.phone_number}')
            elif obj.is_email == True:
                self.message_user(request,'답변 완료 안내문을 발송하였습니다.')
                print(f'{obj.writer}의 이메일: {obj.email}')
            elif obj.is_phone == True:
                self.message_user(request,'답변 완료 안내문을 발송하였습니다.')
                print(f'{obj.writer}의 전화번호: {obj.phone_number}')
            else:
                self.message_user(request,'답변 완료 안내문을 발송할 수 없습니다.', messages.ERROR)
                print('이 문의글은 안내문을 발송할 수 없습니다.')

    actions = [send_inquiry_closed_message]
    send_inquiry_closed_message.short_description = '답변 완료 안내문 발송'

    
