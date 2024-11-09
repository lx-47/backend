# Generated by Django 5.1.1 on 2024-11-07 05:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0015_remove_assessment_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='assessment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='lms.assessment'),
        ),
    ]