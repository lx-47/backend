# Generated by Django 5.1.1 on 2024-11-11 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0040_alter_comment_course_alter_comment_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutor',
            name='detailed_bio',
            field=models.TextField(default=''),
        ),
    ]
