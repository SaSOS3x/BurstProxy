# Generated by Django 4.2 on 2023-05-18 06:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0027_alter_news_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.RemoveField(
            model_name='news',
            name='view',
        ),
        migrations.AddField(
            model_name='news',
            name='view',
            field=models.OneToOneField(default='0', on_delete=django.db.models.deletion.CASCADE, to='blog.ip'),
        ),
    ]
