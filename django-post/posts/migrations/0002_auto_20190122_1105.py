# Generated by Django 2.1.5 on 2019-01-22 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='update_at',
            field=models.DateTimeField(auto_now=True, verbose_name='更新時間'),
        ),
    ]