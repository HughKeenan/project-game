# Generated by Django 4.2.16 on 2024-10-08 11:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_alter_thread_options_rename_title_thread_heading'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='response',
            options={'ordering': ['-posted_on']},
        ),
        migrations.RenameField(
            model_name='thread',
            old_name='heading',
            new_name='title',
        ),
    ]