# Generated by Django 2.2.7 on 2020-02-15 06:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0008_userid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userid',
            name='answer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='study.Useranswer'),
        ),
    ]