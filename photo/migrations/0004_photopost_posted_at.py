# Generated by Django 4.1.4 on 2022-12-27 06:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0003_alter_photopost_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='photopost',
            name='posted_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='投稿日時'),
            preserve_default=False,
        ),
    ]
