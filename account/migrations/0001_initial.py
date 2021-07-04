# Generated by Django 3.2.5 on 2021-07-04 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Bio', models.DateTimeField(auto_now_add=True)),
                ('Name', models.CharField(max_length=300, unique=True)),
                ('Email', models.CharField(max_length=200, unique=True)),
                ('Phone', models.CharField(max_length=8, unique=True)),
                ('Password', models.CharField(max_length=12)),
            ],
            options={
                'ordering': ['Email'],
            },
        ),
    ]
