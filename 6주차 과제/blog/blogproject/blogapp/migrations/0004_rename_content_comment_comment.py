# Generated by Django 4.0.4 on 2022-05-25 07:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0003_alter_blog_photo_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='content',
            new_name='comment',
        ),
    ]
