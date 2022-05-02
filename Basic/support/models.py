from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator

User = get_user_model()

# Create your models here.

# 자주 묻는 질문 Faq
class Faq(models.Model):
    title = models.CharField('제목', max_length=200, default='제목을 입력해주세요')
    question = models.TextField('질문 내용')
    # choices에 들어갈 변수들 정의
    GENERAL = 'general'
    ACCOUNT = 'account'
    ETCETERA = 'etc'

    # choices 튜플 리스트 생성
    CATEGORY_CHOICES = [
        (GENERAL, '일반'),
        (ACCOUNT, '계정'),
        (ETCETERA, '기타'),
    ]
    category = models.CharField(
        '카테고리', 
        max_length=15, 
        choices=CATEGORY_CHOICES, 
        default=GENERAL
    )
    answer = models.TextField('답변 내용')
    writer = models.ForeignKey(
        to=User, 
        on_delete=models.CASCADE, 
        verbose_name='작성자'
    )
    created_at = models.DateTimeField('작성일시', auto_now_add=True)
    updater = models.ManyToManyField(
        to=User, 
        verbose_name='최종 수정자', 
        related_name='updated_faqs',
        blank=True,
    )
    updated_at = models.DateTimeField('최종 수정일시', auto_now=True)

# 1대1 문의 Inquiry
class Inquiry(models.Model):
    # choices에 들어갈 변수들 정의
    GENERAL = 'general'
    ACCOUNT = 'account'
    ETCETERA = 'etc'

    # choices 튜플 리스트 생성
    CATEGORY_CHOICES = [
        (GENERAL, '일반'),
        (ACCOUNT, '계정'),
        (ETCETERA, '기타'),
    ]
    category = models.CharField(
        '카테고리', 
        max_length=15, 
        choices=CATEGORY_CHOICES, 
        default=GENERAL
    )
    title = models.CharField('제목', max_length=200, default='제목을 입력해주세요')
    content = models.TextField('내용')
    image = models.ImageField(verbose_name='이미지', null=True, blank=True)
    email = models.EmailField()
    phone_number_regex = RegexValidator(
        regex=r'^01([0|1|6|7|8|9])-?([0-9]{3,4})-?([0-9]{4})$'
    )
    phone_number = models.CharField('전화번호', max_length=13)
    is_email = models.BooleanField('이메일 수신 여부', default=False)
    is_phone = models.BooleanField('문제메세지 수신 여부', default=False)
    created_at = models.DateTimeField('작성일시', auto_now_add=True)
    updated_at = models.DateTimeField('최종 수정일시', auto_now=True)
    writer = models.ForeignKey(
        to=User, 
        on_delete=models.CASCADE, 
        verbose_name='작성자'
    )
    updater = models.ManyToManyField(
        to=User, 
        verbose_name='최종 수정자', 
        related_name='updated_inquiries',
        blank=True,
    )

# 답변 Answer
class Answer(models.Model):
    content = models.TextField('답변 내용', blank=True)
    inquiry = models.ForeignKey(
        to=Inquiry, 
        verbose_name='참조 문의글', 
        on_delete=models.CASCADE
    )
    writer = models.ForeignKey(
        to=User, 
        on_delete=models.CASCADE, 
        verbose_name='답변 작성자',
        blank=True
    )
    created_at = models.DateTimeField('답변 작성일시', auto_now_add=True)
    updated_at = models.DateTimeField('최종 수정일시', auto_now=True)
    updater = models.ManyToManyField(
        to=User, 
        verbose_name='최종 수정자', 
        related_name='updated_answers',
        blank=True,
    )