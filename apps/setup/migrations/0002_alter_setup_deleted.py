# Generated by Django 3.2.11 on 2022-01-14 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setup', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setup',
            name='deleted',
            field=models.BooleanField(default=False, editable=False),
        ),
    ]