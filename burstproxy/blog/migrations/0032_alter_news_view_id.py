# Generated by Django 4.2 on 2023-05-18 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0031_remove_news_view_id_news_view_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='view_id',
            field=models.CharField(max_length=100),
        ),
    ]
