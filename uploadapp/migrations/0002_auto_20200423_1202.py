# Generated by Django 3.0.5 on 2020-04-23 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploadapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='file',
            field=models.ImageField(default=1, upload_to='media/'),
            preserve_default=False,
        ),
    ]