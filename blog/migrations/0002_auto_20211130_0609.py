# Generated by Django 3.2.9 on 2021-11-30 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='counted_view',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]