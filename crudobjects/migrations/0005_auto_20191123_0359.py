# Generated by Django 2.2.3 on 2019-11-23 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudobjects', '0004_auto_20191123_0245'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='crudobject',
            index=models.Index(fields=['id'], name='id_index'),
        ),
    ]
