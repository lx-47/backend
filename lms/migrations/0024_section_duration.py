# Generated by Django 5.1.1 on 2024-11-08 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0023_alter_course_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='duration',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
