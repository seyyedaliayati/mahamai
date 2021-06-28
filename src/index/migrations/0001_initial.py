# Generated by Django 3.2.3 on 2021-06-28 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=256)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Contact Us Data',
            },
        ),
        migrations.CreateModel(
            name='WorkWithUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=20)),
                ('first_name', models.CharField(max_length=130)),
                ('last_name', models.CharField(max_length=130)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=30)),
                ('message', models.TextField()),
                ('resume_file', models.FileField(blank=True, null=True, upload_to='work-with-us/')),
            ],
            options={
                'verbose_name_plural': 'Work with Us Data',
            },
        ),
    ]
