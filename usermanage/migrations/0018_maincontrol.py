# Generated by Django 3.0.7 on 2020-08-03 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usermanage', '0017_auto_20200803_1356'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainControl',
            fields=[
                ('controlid', models.AutoField(primary_key=True, serialize=False)),
                ('controlname', models.CharField(max_length=45)),
                ('controlpwd', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'MainControl',
            },
        ),
    ]
