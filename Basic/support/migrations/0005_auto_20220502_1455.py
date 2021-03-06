# Generated by Django 3.2.13 on 2022-05-02 14:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('support', '0004_auto_20220502_1307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='content',
            field=models.TextField(blank=True, verbose_name='답변 내용'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='writer',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='답변 작성자'),
        ),
    ]
