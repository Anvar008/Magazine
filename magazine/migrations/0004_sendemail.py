# Generated by Django 5.1.2 on 2024-11-11 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0003_post_author_job'),
    ]

    operations = [
        migrations.CreateModel(
            name='SendEmail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
    ]
