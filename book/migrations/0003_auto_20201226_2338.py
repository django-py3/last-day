# Generated by Django 3.1.4 on 2020-12-26 20:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_book_author'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['-pk'], 'verbose_name': 'Book', 'verbose_name_plural': 'Book'},
        ),
    ]
