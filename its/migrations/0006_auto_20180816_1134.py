# Generated by Django 2.0.8 on 2018-08-16 15:34

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('its', '0005_auto_20180815_1414'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('date', models.DateField(auto_now_add=True)),
                ('operation', models.CharField(choices=[('Add', 'ADD'), ('Transfer', 'TRANSFER'), ('Remove', 'REMOVE'), ('Change Status', 'CHANGE STATUS')], max_length=14)),
                ('remarks', models.CharField(blank=True, max_length=200, null=True)),
                ('location', models.CharField(max_length=120)),
                ('proprietor', models.CharField(max_length=30)),
                ('status', models.CharField(choices=[('Active', 'ACTIVE'), ('Inactive', 'INACTIVE'), ('Not Working', 'NOT WORKING'), ('Disposed', 'DISPOSED')], max_length=12)),
            ],
        ),
        migrations.RemoveField(
            model_name='add',
            name='iid',
        ),
        migrations.RemoveField(
            model_name='add',
            name='sid',
        ),
        migrations.RemoveField(
            model_name='dispose',
            name='iid',
        ),
        migrations.RemoveField(
            model_name='dispose',
            name='sid',
        ),
        migrations.RemoveField(
            model_name='remove',
            name='iid',
        ),
        migrations.RemoveField(
            model_name='remove',
            name='sid',
        ),
        migrations.RemoveField(
            model_name='transfer',
            name='iid',
        ),
        migrations.RemoveField(
            model_name='transfer',
            name='sid',
        ),
        migrations.RemoveField(
            model_name='inventory',
            name='location',
        ),
        migrations.RemoveField(
            model_name='inventory',
            name='proprietor',
        ),
        migrations.RemoveField(
            model_name='inventory',
            name='status',
        ),
        migrations.DeleteModel(
            name='Add',
        ),
        migrations.DeleteModel(
            name='Dispose',
        ),
        migrations.DeleteModel(
            name='Remove',
        ),
        migrations.DeleteModel(
            name='Transfer',
        ),
        migrations.AddField(
            model_name='transactions',
            name='iid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='its.Inventory'),
        ),
        migrations.AddField(
            model_name='transactions',
            name='sid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='its.Staff'),
        ),
    ]
