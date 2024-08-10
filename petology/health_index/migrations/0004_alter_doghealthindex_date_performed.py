from django.db import migrations, models

def convert_datetime_to_date(apps, schema_editor):
    DogHealthIndex = apps.get_model('health_index', 'DogHealthIndex')
    for index in DogHealthIndex.objects.all():
        if isinstance(index.date_performed, datetime.datetime):
            index.date_performed = index.date_performed.date()
            index.save()

class Migration(migrations.Migration):

    dependencies = [
        ('health_index', '0003_healthindexbatch_frequency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doghealthindex',
            name='date_performed',
            field=models.DateField(),
        ),
        migrations.RunPython(convert_datetime_to_date),
    ]
