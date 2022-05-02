# Generated by Django 3.2.13 on 2022-05-02 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='inquiry',
            name='status',
            field=models.CharField(choices=[('enquire', '문의 등록'), ('accept', '접수 완료'), ('close', '답변 완료')], default='enquire', max_length=15, verbose_name='상태'),
        ),
    ]
