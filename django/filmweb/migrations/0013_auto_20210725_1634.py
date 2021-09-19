# Generated by Django 3.2.4 on 2021-07-25 14:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('filmweb', '0012_auto_20210725_1629'),
    ]

    operations = [
        migrations.AddField(
            model_name='ocena',
            name='autor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dodatkoweinfo',
            name='gatunek',
            field=models.PositiveSmallIntegerField(choices=[(4, 'Drama'), (3, 'Komedia'), (2, 'Sci-fi'), (1, 'Horror'), (0, 'Inne')], default=0),
        ),
    ]
