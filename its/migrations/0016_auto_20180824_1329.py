# Generated by Django 2.0.8 on 2018-08-24 17:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('its', '0015_auto_20180824_1048'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='transactions',
            options={'ordering': ['-date']},
        ),
    ]
