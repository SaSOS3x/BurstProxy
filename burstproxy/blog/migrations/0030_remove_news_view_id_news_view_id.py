# Generated by Django 4.2 on 2023-05-18 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0029_rename_view_news_view_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='view_id',
        ),
        migrations.AddField(
            model_name='news',
            name='view_id',
            field=models.ManyToManyField(related_name='view_id', to='blog.ip'),
        ),
    ]