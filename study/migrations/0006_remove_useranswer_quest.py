# Generated by Django 2.2.7 on 2020-02-07 09:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0005_useranswer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useranswer',
            name='quest',
        ),
    ]