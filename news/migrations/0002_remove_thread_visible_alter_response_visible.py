# Generated by Django 4.2.16 on 2024-10-29 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='thread',
            name='visible',
        ),
        migrations.AlterField(
            model_name='response',
            name='visible',
            field=models.BooleanField(default=True),
        ),
    ]