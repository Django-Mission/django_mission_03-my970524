# Generated by Django 3.2.13 on 2022-05-02 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0002_auto_20220502_1053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='μμ±μΌμ'),
        ),
    ]
