# Generated by Django 5.1.1 on 2024-11-11 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0036_remove_student_program_remove_student_year_of_study_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courserating',
            name='rating',
            field=models.PositiveIntegerField(default=0),
        ),
    ]