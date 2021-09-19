# Generated by Django 3.2.4 on 2021-07-25 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmweb', '0018_alter_dodatkoweinfo_gatunek'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dodatkoweinfo',
            name='gatunek',
            field=models.PositiveSmallIntegerField(choices=[(4, 'Drama'), (0, 'Inne'), (3, 'Komedia'), (1, 'Horror'), (2, 'Sci-fi')], default=0),
        ),
        migrations.AlterField(
            model_name='ocena',
            name='autor',
            field=models.CharField(blank=True, default=2, max_length=64, null=True),
        ),
    ]
