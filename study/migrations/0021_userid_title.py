# Generated by Django 2.2.7 on 2020-02-16 12:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0020_remove_userid_test'),
    ]

    operations = [
        migrations.AddField(
            model_name='userid',
            name='title',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='study.Test'),
            preserve_default=False,
        ),
    ]
