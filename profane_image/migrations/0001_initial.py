# Generated by Django 3.1.6 on 2021-05-16 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InputImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('inputImage', models.ImageField(blank=True, upload_to='inputImages/%Y/%m/%d/')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
