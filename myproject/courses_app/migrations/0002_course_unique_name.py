# Generated by Django 4.2.10 on 2024-02-20 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses_app', '0001_initial'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='course',
            constraint=models.UniqueConstraint(fields=('name',), name='unique_name'),
        ),
    ]