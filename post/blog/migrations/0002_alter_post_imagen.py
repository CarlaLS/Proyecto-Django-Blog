# Generated by Django 4.0.4 on 2022-06-04 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='imagen',
            field=models.URLField(max_length=260),
        ),
    ]
