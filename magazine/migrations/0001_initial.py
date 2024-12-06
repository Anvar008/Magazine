# Generated by Django 5.1.2 on 2024-11-09 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='posts_image/')),
                ('category', models.CharField(max_length=221)),
                ('title', models.CharField(max_length=221)),
                ('description', models.TextField()),
                ('author_image', models.CharField(max_length=221)),
                ('author_name', models.CharField(max_length=221)),
                ('post_add_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
