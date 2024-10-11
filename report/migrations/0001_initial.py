# Generated by Django 4.2.16 on 2024-10-11 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thread_url', models.URLField()),
                ('reported_user', models.CharField()),
                ('reason_for_report', models.TextField()),
                ('reporter_username', models.CharField()),
                ('reporter_email', models.EmailField(max_length=254)),
            ],
        ),
    ]