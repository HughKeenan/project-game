# Generated by Django 4.2.16 on 2024-10-18 11:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='response',
            options={'ordering': ['posted_on']},
        ),
    ]
