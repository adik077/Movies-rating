# Generated by Django 3.2.4 on 2021-07-25 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmweb', '0024_auto_20210725_1716'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ocena',
            name='autor',
        ),
        migrations.AlterField(
            model_name='dodatkoweinfo',
            name='gatunek',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Inne'), (4, 'Drama'), (2, 'Sci-fi'), (1, 'Horror'), (3, 'Komedia')], default=0),
        ),
    ]
