# Generated by Django 4.0.3 on 2022-07-22 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0004_alter_feedback_name_alter_feedback_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='rating',
            field=models.PositiveIntegerField(),
        ),
    ]
