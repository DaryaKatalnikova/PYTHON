# Generated by Django 2.2.7 on 2020-02-15 07:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0017_auto_20200215_1251'),
    ]

    operations = [
        migrations.AddField(
            model_name='userid',
            name='test',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='study.Test'),
            preserve_default=False,
        ),
    ]