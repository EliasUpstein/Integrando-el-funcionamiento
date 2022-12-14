# Generated by Django 4.1 on 2022-08-13 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cuenta',
            fields=[
                ('account_id', models.AutoField(primary_key=True, serialize=False)),
                ('balance', models.IntegerField()),
                ('iban', models.TextField()),
                ('account_type', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'cuenta',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Movimientos',
            fields=[
                ('transaction_id', models.AutoField(primary_key=True, serialize=False)),
                ('account_id', models.IntegerField()),
                ('operation_tipe', models.TextField()),
                ('amount', models.IntegerField()),
                ('changed_at', models.TextField()),
            ],
            options={
                'db_table': 'movimientos',
                'managed': False,
            },
        ),
    ]
