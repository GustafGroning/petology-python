# Generated by Django 3.2.23 on 2024-06-13 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health_records', '0003_auto_20240613_1055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='condition',
            name='follow_up_date',
            field=models.DateField(null=True),
        ),
    ]