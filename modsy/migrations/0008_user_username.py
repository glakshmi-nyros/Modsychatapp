# Generated by Django 3.0.1 on 2020-01-07 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modsy', '0007_auto_20200106_1219'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
    ]
