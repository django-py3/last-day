# Generated by Django 3.1.4 on 2020-12-26 20:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0003_auto_20201226_2346'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='journal',
            options={'ordering': ['-journalspagecount']},
        ),
    ]
