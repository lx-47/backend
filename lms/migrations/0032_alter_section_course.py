# Generated by Django 5.1.1 on 2024-11-11 09:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0031_alter_course_description_alter_course_duration_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sections', to='lms.course'),
        ),
    ]