# Generated by Django 4.2 on 2023-05-17 16:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_remove_news_view_news_view_set'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='view_set',
            new_name='view',
        ),
    ]
