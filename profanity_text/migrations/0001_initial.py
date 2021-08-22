# Generated by Django 3.1.6 on 2021-04-09 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cusslist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cussword', models.CharField(max_length=100, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('edited', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['cussword'],
            },
        ),
    ]
