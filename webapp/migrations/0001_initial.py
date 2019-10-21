# Generated by Django 2.0.1 on 2018-01-20 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TmbinCustomer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('mobile', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True, unique=True)),
                ('email', models.CharField(blank=True, max_length=30, null=True)),
                ('business_name', models.CharField(blank=True, max_length=50, null=True)),
                ('address', models.CharField(blank=True, max_length=50, null=True)),
                ('gst_no', models.CharField(blank=True, db_column='GST_NO', max_length=25, null=True)),
                ('description', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'tmbin_customer',
            },
        ),
        migrations.CreateModel(
            name='TmbinTable',
            fields=[
                ('table_no', models.IntegerField(primary_key=True, serialize=False)),
                ('is_available', models.IntegerField()),
                ('table_name', models.CharField(blank=True, db_column='TABLE_NAME', max_length=25, null=True, unique=True)),
            ],
            options={
                'managed': False,
                'db_table': 'tmbin_table',
            },
        ),
    ]