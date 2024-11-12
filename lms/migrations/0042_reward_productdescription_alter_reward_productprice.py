# Generated by Django 5.1.1 on 2024-11-11 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0041_tutor_detailed_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='reward',
            name='productDescription',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='reward',
            name='productPrice',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True),
        ),
    ]