# Generated by Django 3.0.6 on 2020-05-30 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200530_1345'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default=0, max_length=30),
            preserve_default=False,
        ),
    ]
