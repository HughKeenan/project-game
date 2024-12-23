# Generated by Django 4.2.16 on 2024-10-29 13:49

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
                ('title', models.CharField(max_length=250)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ReportUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thread_url', models.URLField()),
                ('user_being_reported', models.CharField(max_length=250)),
                ('reason_for_report', models.TextField()),
                ('reporters_email', models.EmailField(max_length=254)),
                ('examined', models.BooleanField(default=False)),
            ],
        ),
    ]
