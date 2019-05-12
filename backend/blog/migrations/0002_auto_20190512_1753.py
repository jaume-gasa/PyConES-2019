# Generated by Django 2.2.1 on 2019-05-12 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.CharField(default='Jaume Gasa', max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='external_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.CharField(default='hola', max_length=2000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='lang',
            field=models.CharField(default='es', max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='short_description',
            field=models.TextField(default='short desc'),
            preserve_default=False,
        ),
    ]
