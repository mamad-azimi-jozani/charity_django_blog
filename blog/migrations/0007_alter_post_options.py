# Generated by Django 3.2.9 on 2021-12-13 05:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20211206_0739'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['published_date']},
        ),
    ]