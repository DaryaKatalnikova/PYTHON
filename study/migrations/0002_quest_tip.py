# Generated by Django 2.2.7 on 2019-11-20 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quest',
            name='tip',
            field=models.CharField(default=1, max_length=1),
            preserve_default=False,
        ),
    ]
