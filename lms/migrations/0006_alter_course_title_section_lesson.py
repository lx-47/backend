# Generated by Django 5.1.1 on 2024-11-05 09:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0005_todo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='title',
            field=models.CharField(max_length=255),
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lms.course')),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('duration', models.PositiveIntegerField(blank=True, null=True)),
                ('content_type', models.CharField(choices=[('reading', 'Reading'), ('video', 'Video')], max_length=10, null=True)),
                ('content', models.CharField(blank=True, max_length=1000, null=True)),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lms.section')),
            ],
        ),
    ]
