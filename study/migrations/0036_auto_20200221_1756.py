# Generated by Django 2.2.7 on 2020-02-21 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0035_auto_20200221_1749'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='userid',
        ),
        migrations.AddField(
            model_name='user',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(default=123, max_length=200),
            preserve_default=False,
        ),
    ]
