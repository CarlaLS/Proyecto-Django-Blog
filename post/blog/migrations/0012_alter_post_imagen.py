# Generated by Django 4.0.4 on 2022-06-06 12:48

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_comentarios_remove_post_categoria_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='imagen',
            field=models.ImageField(default='default.png', upload_to='post', validators=[django.core.validators.FileExtensionValidator(['png', 'jpg'])]),
        ),
    ]
