# Generated by Django 4.2 on 2023-05-18 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0020_remove_news_view'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='id',
            field=models.IntegerField(default=0, primary_key=True, serialize=False, unique=True),
        ),
    ]
