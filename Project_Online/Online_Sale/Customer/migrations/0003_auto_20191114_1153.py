# Generated by Django 2.2.3 on 2019-11-14 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0002_remove_registerdata_id_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registerdata',
            name='contact',
            field=models.CharField(max_length=10),
        ),
    ]
