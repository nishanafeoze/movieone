# Generated by Django 4.2.1 on 2023-05-31 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0004_rename_dec_movie_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='img',
            field=models.ImageField(default='ddffddrs', upload_to='gallery'),
            preserve_default=False,
        ),
    ]
