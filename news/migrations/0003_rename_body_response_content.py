# Generated by Django 4.2.16 on 2024-10-24 17:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_alter_response_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='response',
            old_name='body',
            new_name='content',
        ),
    ]