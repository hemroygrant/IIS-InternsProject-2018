# Generated by Django 2.0.8 on 2018-08-20 13:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('its', '0009_auto_20180817_1450'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='transactions',
            options={'ordering': ['date']},
        ),
    ]
