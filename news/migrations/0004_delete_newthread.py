# Generated by Django 4.2.16 on 2024-10-27 16:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_rename_body_response_content'),
    ]

    operations = [
        migrations.DeleteModel(
            name='NewThread',
        ),
    ]
