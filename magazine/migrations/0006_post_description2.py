# Generated by Django 5.1.2 on 2024-11-14 12:54

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0005_alter_post_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='description2',
            field=ckeditor.fields.RichTextField(default=123),
            preserve_default=False,
        ),
    ]
