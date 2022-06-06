# Generated by Django 4.0.4 on 2022-06-05 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_remove_post_fecha_publicacion_remove_post_publicado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='descripcion',
        ),
        migrations.RemoveField(
            model_name='post',
            name='slug',
        ),
        migrations.AlterField(
            model_name='post',
            name='subtitulo',
            field=models.CharField(max_length=250, unique=True, verbose_name='Subtitulo'),
        ),
        migrations.AlterField(
            model_name='post',
            name='titulo',
            field=models.CharField(max_length=150, unique=True, verbose_name='Titulo'),
        ),
    ]
