# Generated by Django 4.2 on 2023-05-18 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0030_remove_news_view_id_news_view_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='view_id',
        ),
        migrations.AddField(
            model_name='news',
            name='view_id',
            field=models.CharField(default='0', max_length=100, unique=True),
        ),
    ]
