# Generated by Django 3.2.4 on 2021-07-26 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmweb', '0026_auto_20210726_1050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dodatkoweinfo',
            name='gatunek',
            field=models.PositiveSmallIntegerField(choices=[(2, 'Sci-fi'), (3, 'Komedia'), (4, 'Drama'), (0, 'Inne'), (1, 'Horror')], default=0),
        ),
    ]