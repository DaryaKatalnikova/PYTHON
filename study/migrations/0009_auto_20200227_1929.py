# Generated by Django 3.0.3 on 2020-02-27 14:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0008_auto_20200227_1819'),
    ]

    operations = [
        migrations.RenameField(
            model_name='useranswer',
            old_name='id_user',
            new_name='user',
        ),
    ]
