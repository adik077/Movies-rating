# Generated by Django 3.2.4 on 2021-07-26 11:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmweb', '0034_auto_20210726_1301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dodatkoweinfo',
            name='gatunek',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Horror'), (2, 'Sci-fi'), (4, 'Drama'), (0, 'Inne'), (3, 'Komedia')], default=0),
        ),
        migrations.AlterField(
            model_name='ocena',
            name='gwiazdki',
            field=models.PositiveSmallIntegerField(default=5, validators=[django.core.validators.MaxValueValidator(0), django.core.validators.MinValueValidator(5)]),
        ),
    ]
