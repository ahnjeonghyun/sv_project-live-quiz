# Generated by Django 3.2 on 2021-05-28 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identification', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'admins',
            },
        ),
    ]
