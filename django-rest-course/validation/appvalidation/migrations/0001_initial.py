# Generated by Django 3.2.4 on 2021-06-08 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('studentId', models.IntegerField()),
                ('address', models.CharField(max_length=30)),
            ],
        ),
    ]
