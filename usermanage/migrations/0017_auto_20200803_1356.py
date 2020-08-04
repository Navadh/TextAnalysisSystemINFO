# Generated by Django 3.0.7 on 2020-08-03 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usermanage', '0016_textadmin'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('admin_id', models.AutoField(primary_key=True, serialize=False)),
                ('admin_name', models.CharField(max_length=45)),
                ('admin_pwd', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'Admin',
            },
        ),
        migrations.RenameField(
            model_name='textadmin',
            old_name='tadmin_id',
            new_name='textadmin_id',
        ),
        migrations.RenameField(
            model_name='textadmin',
            old_name='tadmin_name',
            new_name='textadmin_name',
        ),
        migrations.RenameField(
            model_name='textadmin',
            old_name='tadmin_pwd',
            new_name='textadmin_pwd',
        ),
    ]