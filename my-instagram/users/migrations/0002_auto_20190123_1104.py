# Generated by Django 2.1.5 on 2019-01-23 03:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Relationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_agree', models.BooleanField(default=False, verbose_name='同意')),
                ('is_deleted', models.BooleanField(default=True, verbose_name='顯示')),
                ('start_at', models.DateTimeField(auto_now=True, verbose_name='開始時間')),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='introduction',
            field=models.BooleanField(blank=True, verbose_name='自我介紹'),
        ),
        migrations.AddField(
            model_name='relationship',
            name='from_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='following', to=settings.AUTH_USER_MODEL, verbose_name='從'),
        ),
        migrations.AddField(
            model_name='relationship',
            name='to_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follower', to=settings.AUTH_USER_MODEL, verbose_name='到'),
        ),
        migrations.AlterUniqueTogether(
            name='relationship',
            unique_together={('from_user', 'to_user')},
        ),
    ]
