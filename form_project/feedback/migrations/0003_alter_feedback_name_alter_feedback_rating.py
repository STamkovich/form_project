# Generated by Django 4.0.3 on 2022-04-17 11:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0002_alter_feedback_feedback_alter_feedback_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='name',
            field=models.CharField(max_length=40, validators=[django.core.validators.MinValueValidator(3)]),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='rating',
            field=models.PositiveSmallIntegerField(validators=[django.core.validators.MaxLengthValidator(100)]),
        ),
    ]