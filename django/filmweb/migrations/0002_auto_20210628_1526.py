# Generated by Django 3.2.4 on 2021-06-28 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmweb', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='rok',
            field=models.PositiveSmallIntegerField(default=2000),
        ),
        migrations.AlterField(
            model_name='film',
            name='tytul',
            field=models.CharField(max_length=64, unique=True),
        ),
    ]
