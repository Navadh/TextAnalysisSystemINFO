# Generated by Django 3.0.5 on 2020-07-14 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TextMange',
            fields=[
                ('ttextmanageid', models.AutoField(primary_key=True, serialize=False)),
                ('userid', models.IntegerField()),
                ('updatetime', models.DateTimeField()),
                ('ptype', models.CharField(max_length=45)),
                ('pname', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'TTextManage',
            },
        ),
    ]
